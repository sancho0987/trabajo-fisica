"""Ejecuta el experimento de lectura/escritura de archivos de auditoría."""
from __future__ import annotations

import argparse
import csv
import json
import os
import platform
import statistics
import sys
import tempfile
import time
from pathlib import Path

from src.estrategias import buffered, texto_lineas
from src.linea_base import ejecutar as ejecutar_linea_base


def ejecutar(eventos: int, bytes_por_evento: int, repeticiones: int,
             bloques: list[int], carpeta: str = "resultados") -> list[dict]:
    destino = Path(carpeta)
    destino.mkdir(parents=True, exist_ok=True)
    metodos = [("linea_base", None), *[(f"buffer_{b}", b) for b in bloques], ("texto_lineas", None)]
    registros: list[dict] = []
    referencia = None
    for nombre, bloque in metodos:
        for repeticion in range(1, repeticiones + 1):
            with tempfile.TemporaryDirectory(prefix="experimento_io_") as temporal:
                ruta = Path(temporal) / "auditoria.log"
                cpu_inicio = time.process_time()
                pared_inicio = time.perf_counter()
                if nombre == "linea_base":
                    resultado = ejecutar_linea_base(ruta, eventos, bytes_por_evento)
                    bytes_leidos, sha256 = resultado["bytes_leidos"], resultado["sha256"]
                elif nombre == "texto_lineas":
                    bytes_leidos, sha256 = texto_lineas(ruta, eventos, bytes_por_evento)
                else:
                    bytes_leidos, sha256 = buffered(ruta, eventos, bytes_por_evento, bloque)
                segundos = time.perf_counter() - pared_inicio
                cpu = time.process_time() - cpu_inicio
            if referencia is None:
                referencia = (bytes_leidos, sha256)
            if (bytes_leidos, sha256) != referencia:
                raise AssertionError(f"{nombre} produjo contenido distinto a la línea base")
            mib_s = bytes_leidos / (1024 * 1024) / segundos if segundos else 0.0
            registros.append({
                "eventos": eventos, "bytes_por_evento": bytes_por_evento,
                "bytes_leidos": bytes_leidos, "estrategia": nombre,
                "tamano_bloque": bloque or "", "repeticion": repeticion,
                "tiempo_segundos": segundos, "cpu_segundos": cpu,
                "tasa_mib_s": mib_s, "sha256": sha256,
            })
            print(f"{nombre:>14} | repetición {repeticion}/{repeticiones} | "
                  f"{segundos:.6f} s | {mib_s:.2f} MiB/s | {bytes_leidos} bytes")

    campos = list(registros[0]) if registros else []
    with (destino / "resultados.csv").open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(registros)
    (destino / "resultados.json").write_text(json.dumps(registros, ensure_ascii=False, indent=2), encoding="utf-8")
    entorno = {
        "sistema": platform.system(), "version_sistema": platform.version(),
        "arquitectura": platform.machine(), "procesador": platform.processor(),
        "python": sys.version, "cpu_logicas": os.cpu_count(),
        "directorio_temporal": tempfile.gettempdir(),
        "nota_cache": "Las lecturas pueden servirse desde la caché de páginas del sistema operativo.",
    }
    (destino / "entorno.json").write_text(json.dumps(entorno, ensure_ascii=False, indent=2), encoding="utf-8")
    resumen = {}
    for nombre, _ in metodos:
        tiempos = [r["tiempo_segundos"] for r in registros if r["estrategia"] == nombre]
        resumen[nombre] = {
            "media_segundos": statistics.mean(tiempos),
            "mediana_segundos": statistics.median(tiempos),
            "desviacion_estandar_segundos": statistics.stdev(tiempos) if len(tiempos) > 1 else 0.0,
        }
    (destino / "resumen.json").write_text(json.dumps(resumen, ensure_ascii=False, indent=2), encoding="utf-8")
    _guardar_grafico(resumen, destino / "comparacion.svg")
    return registros


def _guardar_grafico(resumen: dict, ruta: Path) -> None:
    nombres = list(resumen)
    valores = [resumen[n]["mediana_segundos"] for n in nombres]
    maximo = max(valores, default=0) or 1
    ancho, alto, margen = 760, 90 + 42 * len(nombres), 180
    filas = []
    for i, (nombre, valor) in enumerate(zip(nombres, valores)):
        y = 45 + i * 42
        largo = 500 * valor / maximo
        filas.append(f'<text x="{margen-10}" y="{y+18}" text-anchor="end">{nombre}</text>'
                     f'<rect x="{margen}" y="{y}" width="{largo:.2f}" height="24" fill="#3478b8"/>'
                     f'<text x="{margen+largo+8:.2f}" y="{y+18}">{valor:.6f} s</text>')
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{ancho}" height="{alto}" viewBox="0 0 {ancho} {alto}">'
           '<rect width="100%" height="100%" fill="white"/><text x="20" y="24" font-size="16">'
           'Mediana del tiempo total (escritura + lectura)</text>' + ''.join(filas) + '</svg>')
    ruta.write_text(svg, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--eventos", type=int, default=5_000)
    parser.add_argument("--bytes-por-evento", type=int, default=64)
    parser.add_argument("--repeticiones", type=int, default=5)
    parser.add_argument("--bloques", type=int, nargs="+", default=[4096, 65536])
    parser.add_argument("--salida", default="resultados")
    args = parser.parse_args()
    if args.eventos < 0 or args.bytes_por_evento < 1 or args.repeticiones < 5 or any(x < 1 for x in args.bloques):
        parser.error("eventos >= 0, bytes_por_evento y bloques >= 1; repeticiones >= 5")
    ejecutar(args.eventos, args.bytes_por_evento, args.repeticiones, args.bloques, args.salida)
    print(f"Resultados guardados en {args.salida}/")


if __name__ == "__main__":
    main()
