"""
Línea base — Equipo 6: Lectura y escritura de archivos.

Situación inicial: el sistema de auditoría registra cada evento ABRIENDO el
archivo, escribiendo una línea y CERRÁNDOLO. Luego, para el reporte diario,
lee el archivo carácter por carácter contando líneas y bytes.

preparar(n) -> (ruta_destino, lista de n eventos de texto)
ejecutar(datos) -> (lineas_leidas, bytes_leidos)

Magnitud derivada clave: TASA DE TRANSFERENCIA = bytes / tiempo  [MB/s]

Cuidado experimental: después de escribir, el sistema operativo guarda el
archivo en su caché de RAM ("page cache"). Una lectura inmediata mide
memoria, no disco. Documente si sus lecturas son "en caliente" o "en frío".
"""
import random
import time
from pathlib import Path

DATOS = Path(__file__).resolve().parents[1] / "datos"


def preparar(n: int, semilla: int = 6):
    rng = random.Random(semilla)
    eventos = [f"2026-10-{rng.randint(1, 31):02d}T{rng.randint(0, 23):02d}:{rng.randint(0, 59):02d};"
               f"usuario{rng.randint(1, 500):03d};{rng.choice(['LOGIN', 'LOGOUT', 'CONSULTA', 'PAGO', 'ERROR'])};"
               f"{rng.random():.8f}\n" for _ in range(n)]
    DATOS.mkdir(parents=True, exist_ok=True)
    return DATOS / f"auditoria_{n}.log", eventos


def ejecutar(datos) -> tuple[int, int]:
    ruta, eventos = datos
    ruta.unlink(missing_ok=True)
    for e in eventos:                                  # 1 apertura + 1 escritura + 1 cierre por evento
        with open(ruta, "a", encoding="utf-8") as f:
            f.write(e)
    lineas = bytes_leidos = 0
    with open(ruta, "rb") as f:
        while (c := f.read(1)):                        # una llamada de lectura por byte
            bytes_leidos += 1
            lineas += c == b"\n"
    return lineas, bytes_leidos


if __name__ == "__main__":
    d = preparar(20_000)
    t0 = time.perf_counter()
    l, b = ejecutar(d)
    t = time.perf_counter() - t0
    print(f"{l} líneas, {b / 1e6:.2f} MB en {t:.2f} s -> {b / 1e6 / t:.2f} MB/s (escritura+lectura)")
