"""Tres estrategias equivalentes: secuencial, hilos y procesos."""
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from src.problema import contar_primos_rango

def _contar_bloque(limites):
    """Función de nivel superior: es serializable para multiprocessing spawn."""
    inicio, fin = limites
    return contar_primos_rango(inicio, fin)

def _dividir_rango(limite: int, partes: int):
    if limite < 2:
        return []
    partes = max(1, min(partes, limite - 1))
    total = limite - 1
    tam = (total + partes - 1) // partes
    bloques = []
    inicio = 2
    while inicio <= limite:
        fin = min(limite, inicio + tam - 1)
        bloques.append((inicio, fin))
        inicio = fin + 1
    return bloques

def estrategia_secuencial(limite: int) -> int:
    return contar_primos_rango(2, limite)

def estrategia_hilos(limite: int, trabajadores: int | None = None) -> int:
    bloques = _dividir_rango(limite, trabajadores or (os_cpu_count() or 2))
    if not bloques:
        return 0
    with ThreadPoolExecutor(max_workers=trabajadores) as executor:
        return sum(executor.map(_contar_bloque, bloques))

def estrategia_procesos(limite: int, trabajadores: int | None = None) -> int:
    bloques = _dividir_rango(limite, trabajadores or (os_cpu_count() or 2))
    if not bloques:
        return 0
    # La creación del pool se ejecuta al llamar esta función, desde el programa protegido
    # por if __name__ == "__main__" en el punto de entrada.
    with ProcessPoolExecutor(max_workers=trabajadores) as executor:
        return sum(executor.map(_contar_bloque, bloques))

def os_cpu_count():
    import os
    return os.cpu_count()
