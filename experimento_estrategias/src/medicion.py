"""Funciones para medir duración sin incluir la preparación del resultado."""
from time import perf_counter

def medir(funcion, *args, **kwargs):
    inicio = perf_counter()
    resultado = funcion(*args, **kwargs)
    duracion = perf_counter() - inicio
    return resultado, duracion
