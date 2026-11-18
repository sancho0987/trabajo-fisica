"""Problema del experimento: contar números primos en un intervalo."""
from math import isqrt

def es_primo(numero: int) -> bool:
    if numero < 2:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    limite = isqrt(numero)
    divisor = 3
    while divisor <= limite:
        if numero % divisor == 0:
            return False
        divisor += 2
    return True

def contar_primos_rango(inicio: int, fin: int) -> int:
    """Cuenta primos en el intervalo inclusivo [inicio, fin]."""
    return sum(1 for n in range(max(2, inicio), fin + 1) if es_primo(n))
