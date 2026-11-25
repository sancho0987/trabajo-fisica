# Entorno de ejecución

El experimento funciona con Python 3.10 o superior y usa únicamente la biblioteca estándar para las estrategias y mediciones.

Registrar sistema operativo, versión, arquitectura, procesador y cantidad de CPU lógicas en `resultados/entorno.json`.

## Monitor opcional
Instalar `psutil` con `pip install psutil`. La lectura de porcentaje de CPU y frecuencia suele estar disponible; la temperatura depende del hardware, los controladores y el sistema operativo. En equipos donde no esté soportada, el campo de temperatura queda vacío/no disponible. El monitor no forma parte del cronometraje principal.
