"""Estrategias equivalentes de escritura y lectura de eventos de auditoría."""
from __future__ import annotations

import hashlib
from pathlib import Path


def _resumen(ruta: Path) -> tuple[int, str]:
    h = hashlib.sha256()
    total = 0
    with ruta.open("rb") as archivo:
        while bloque := archivo.read(64 * 1024):
            total += len(bloque)
            h.update(bloque)
    return total, h.hexdigest()


def _evento(indice: int, bytes_por_evento: int) -> bytes:
    prefijo = f"evento={indice:09d} accion=lectura\n".encode("ascii")
    if len(prefijo) > bytes_por_evento:
        raise ValueError("bytes_por_evento no alcanza para almacenar el registro")
    return prefijo + b"." * (bytes_por_evento - len(prefijo))


def buffered(ruta: str | Path, eventos: int, bytes_por_evento: int, bloque: int) -> tuple[int, str]:
    """Mantiene el archivo abierto, acumula bloques de escritura y lee por bloques."""
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    lote: list[bytes] = []
    usados = 0
    with destino.open("wb", buffering=max(2, bloque)) as archivo:
        for i in range(eventos):
            linea = _evento(i, bytes_por_evento)
            lote.append(linea)
            usados += len(linea)
            if usados >= bloque:
                archivo.writelines(lote)
                lote.clear()
                usados = 0
        if lote:
            archivo.writelines(lote)
    return _resumen(destino)


def texto_lineas(ruta: str | Path, eventos: int, bytes_por_evento: int) -> tuple[int, str]:
    """Mantiene el archivo abierto en modo texto y procesa cada línea."""
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    with destino.open("w", encoding="ascii", newline="\n", buffering=64 * 1024) as archivo:
        for i in range(eventos):
            archivo.write(_evento(i, bytes_por_evento).decode("ascii"))
    digest = hashlib.sha256()
    total = 0
    with destino.open("r", encoding="ascii", newline="") as archivo:
        for linea in archivo:
            datos = linea.encode("ascii")
            total += len(datos)
            digest.update(datos)
    return total, digest.hexdigest()
