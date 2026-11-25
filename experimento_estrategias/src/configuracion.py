"""Configuración central del experimento."""
TAMANOS = [1000, 5000, 10000]
REPETICIONES = 5
TRABAJADORES = None  # None = valor predeterminado del sistema
ESTRATEGIAS = ("secuencial", "hilos", "procesos")
