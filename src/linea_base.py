"""Línea base: abrir/cerrar por evento y leer byte a byte."""
from __future__ import annotations

import argparse
import hashlib
import json
import tempfile
import time
from pathlib import Path
from src.estrategias import _evento


def ejecutar(ruta: str | Path, eventos: int = 5_000, bytes_por_evento: int = 64) -> dict:
    """Escribe eventos en llamadas independientes y luego lee un byte a la vez."""
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    inicio = time.perf_counter()
    cpu_inicio = time.process_time()
    destino.write_bytes(b"")
    for indice in range(eventos):
        contenido = _evento(indice, bytes_por_evento)
        with destino.open("ab") as archivo:
            archivo.write(contenido)
    digest = hashlib.sha256()
    total = 0
    with destino.open("rb") as archivo:
        while byte := archivo.read(1):
            digest.update(byte)
            total += len(byte)
    segundos = time.perf_counter() - inicio
    return {
        "estrategia": "linea_base", "eventos": eventos,
        "bytes_por_evento": bytes_por_evento, "bytes_leidos": total,
        "sha256": digest.hexdigest(), "tiempo_segundos": segundos,
        "cpu_segundos": time.process_time() - cpu_inicio,
        "tasa_mib_s": total / (1024 * 1024) / segundos if segundos else 0.0,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--eventos", type=int, default=5_000)
    parser.add_argument("--bytes-por-evento", type=int, default=64)
    parser.add_argument("--salida", default="resultados/evidencia_linea_base.json")
    args = parser.parse_args()
    if args.eventos < 0 or args.bytes_por_evento < 1:
        parser.error("eventos debe ser >= 0 y bytes-por-evento debe ser >= 1")
    with tempfile.TemporaryDirectory(prefix="experimento_io_") as carpeta:
        resultado = ejecutar(Path(carpeta) / "auditoria.log", args.eventos, args.bytes_por_evento)
    salida = Path(args.salida)
    salida.parent.mkdir(parents=True, exist_ok=True)
    salida.write_text(json.dumps(resultado, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(resultado, ensure_ascii=False, indent=2))
    print(f"Evidencia guardada en: {salida}")


if __name__ == "__main__":
    main()
