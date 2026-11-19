
"""
Estrategia B — Equipo 6: Escritura continua.

Mantiene el archivo abierto durante todo el proceso de escritura.
La lectura se conserva byte por byte para comparar el efecto
de modificar únicamente el método de escritura.
"""
import os
import time
from .linea_base import preparar


def ejecutar(datos) -> tuple[int, int]:
    ruta, eventos = datos
    ruta.unlink(missing_ok=True)

    # Una sola apertura para escribir todos los eventos
    with open(ruta, "w", encoding="utf-8") as f:
        f.writelines(eventos)

    # Se conserva la lectura original byte por byte
    lineas = bytes_leidos = 0

    with open(ruta, "rb") as f:
        while (c := f.read(1)):
            bytes_leidos += 1
            lineas += c == b"\n"

    return lineas, bytes_leidos


if __name__ == "__main__":
    d = preparar(20_000)

    t0 = time.perf_counter()
    lineas, bytes_leidos = ejecutar(d)
    tiempo = time.perf_counter() - t0

    print(f"{lineas} líneas, {bytes_leidos / 1e6:.2f} MB "
          f"en {tiempo:.2f} s -> "
          f"{bytes_leidos / 1e6 / tiempo:.2f} MB/s")

    # Prueba de corrección
    bytes_esperados = sum(len(e.replace("\n", os.linesep).encode("utf-8")) for e in d[1])

    if lineas == len(d[1]) and bytes_leidos == bytes_esperados:
        print("PRUEBA DE CORRECCIÓN: APROBADA")
    else:
        print("PRUEBA DE CORRECCIÓN: FALLIDA")
