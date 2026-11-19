
"""
Estrategia C — Equipo 6: Lectura por bloques.

Conserva la escritura original de la línea base.
Modifica únicamente la lectura para procesar bloques
de bytes en lugar de leer byte por byte.
"""

import os
import time
from .linea_base import preparar


def ejecutar(datos) -> tuple[int, int]:
    ruta, eventos = datos
    ruta.unlink(missing_ok=True)

    # Se conserva la escritura original de la línea base
    for e in eventos:
        with open(ruta, "a", encoding="utf-8") as f:
            f.write(e)

    # Lectura por bloques de 8192 bytes
    lineas = bytes_leidos = 0

    with open(ruta, "rb") as f:
        while True:
            bloque = f.read(8192)

            if not bloque:
                break

            bytes_leidos += len(bloque)
            lineas += bloque.count(b"\n")

    return lineas, bytes_leidos


if __name__ == "__main__":
    d = preparar(20_000)

    t0 = time.perf_counter()
    lineas, bytes_leidos = ejecutar(d)
    tiempo = time.perf_counter() - t0

    print(
        f"{lineas} líneas, {bytes_leidos / 1e6:.2f} MB "
        f"en {tiempo:.2f} s -> "
        f"{bytes_leidos / 1e6 / tiempo:.2f} MB/s"
    )

    # Prueba de corrección
    bytes_esperados = sum(
        len(e.replace("\n", os.linesep).encode("utf-8"))
        for e in d[1]
    )

    if lineas == len(d[1]) and bytes_leidos == bytes_esperados:
        print("PRUEBA DE CORRECCIÓN: APROBADA")
    else:
        print("PRUEBA DE CORRECCIÓN: FALLIDA")
