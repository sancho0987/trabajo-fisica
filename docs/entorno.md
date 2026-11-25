# Registro del entorno

El comando de experimento guarda automáticamente sistema operativo, versión, arquitectura, procesador, versión de Python, CPU lógicas y directorio temporal en `resultados/entorno.json`.

Registrar además manualmente si la lectura se hizo en caliente o en frío. Por defecto las lecturas pueden estar en caliente debido a la caché de páginas del sistema operativo; no se vacía la caché. Para que las ejecuciones sean comparables, usar el mismo equipo, unidad, sistema de archivos, fuente de alimentación y aplicaciones abiertas.

El monitor de CPU no se incluye en el tiempo medido. Si se desea tomar muestras del sistema, `psutil` es opcional (`pip install -r requirements.txt`); temperatura y frecuencia dependen del sistema operativo y del hardware.
