# Protocolo del experimento

## Objetivo
Comparar el tiempo requerido para contar números primos entre 2 y N usando tres estrategias: secuencial (línea base), hilos y procesos.

## Variable independiente
La estrategia de ejecución y el tamaño N.

## Variable dependiente
El tiempo de ejecución en segundos, medido con `time.perf_counter()`.

## Control de corrección
Antes de guardar cada medición, el programa compara el resultado con la estrategia secuencial. Si difiere, detiene el experimento con un error.

## Procedimiento
1. Conectar el equipo a la corriente y cerrar aplicaciones innecesarias.
2. Evitar usar el PC durante las mediciones.
3. Ejecutar las pruebas de corrección: `python -m unittest discover -s pruebas -v`.
4. Ejecutar el experimento: `python -m experimentos.ejecutar_experimento`.
5. Cada combinación de tamaño y estrategia se ejecuta al menos 5 veces (por defecto 5).
6. Revisar `resultados/resultados.csv`, `resultados/resultados.json` y `resultados/entorno.json`.

## Recomendaciones
Usar el mismo equipo, conexión eléctrica, versión de Python y aplicaciones abiertas para todos los casos. Los tiempos pueden variar entre ejecuciones; comparar promedios y dispersión, no una sola medición.

## Conclusiones del experimento

Después de realizar 45 mediciones, distribuidas en tres tamaños de
datos y tres estrategias de ejecución, se obtuvieron los siguientes
resultados:

1. La estrategia secuencial presentó el menor tiempo de ejecución
   en todos los tamaños evaluados.

2. La estrategia con hilos fue más lenta que la secuencial. Esto
   demuestra que el uso de hilos no garantiza una mejora del
   rendimiento en operaciones de cálculo intensivo en Python.

3. La estrategia con procesos presentó los mayores tiempos de
   ejecución, principalmente por los costos de creación,
   comunicación y administración de procesos.

4. Las tres estrategias produjeron los mismos resultados numéricos,
   comprobando la corrección de los cálculos.

5. Se concluye que, para el experimento realizado y los tamaños
   evaluados, la ejecución secuencial fue la alternativa más
   eficiente.

Como trabajo futuro, se recomienda realizar pruebas con tamaños
de datos considerablemente mayores para evaluar si el paralelismo
puede ofrecer ventajas cuando la carga de trabajo aumenta.
