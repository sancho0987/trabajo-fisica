# Variables experimentales – Equipo 6

## 1. Identificación de variables

| Tipo | Variable | Símbolo | Unidad | Valores / rango | Instrumento o forma de obtención | Justificación |
|---|---|---|---|---|---|---|
| Independiente | Estrategia de procesamiento | — | — | A, B, C | Selección del programa ejecutado | Permite comparar los diferentes métodos de lectura y escritura. |
| Independiente | Tamaño de entrada | n | eventos | 20.000 | Función `preparar()` | Permite establecer una cantidad igual de eventos para las comparaciones. |
| Dependiente | Tiempo de ejecución | t | s | Variable según la estrategia | `time.perf_counter()` | Permite medir cuánto tarda cada estrategia en completar el procesamiento. |
| Dependiente | Tasa de transferencia | V | MB/s | Variable según la estrategia | Cantidad de bytes procesados / tiempo | Permite comparar la velocidad de procesamiento de los datos. |
| Controlada | Equipo de cómputo | — | — | Mismo equipo en cada comparación | Registro de características del computador | Evita comparar directamente tiempos obtenidos en equipos con capacidades diferentes. |
| Controlada | Versión de Python | — | — | Misma versión en cada comparación | Comando `py --version` | Evita diferencias relacionadas con la versión del intérprete. |
| Controlada | Alimentación eléctrica | — | — | Corriente o batería | Registro de las condiciones del equipo | Evita cambios de rendimiento relacionados con el modo de alimentación. |
| Controlada | Programas abiertos | — | — | Sin programas innecesarios | Verificación antes de ejecutar | Reduce la interferencia de otros procesos. |
| Controlada | Datos de entrada | — | — | 20.000 eventos, semilla 6 | Función `preparar()` | Garantiza que las estrategias procesen información equivalente. |
| Controlada | Estado de la caché | — | — | Lectura en caliente | Documentación de las condiciones de ejecución | Permite mantener condiciones de lectura comparables. |

**Nota:** No se medirán directamente el consumo de energía, la temperatura, el uso de CPU ni el pico de memoria en esta fase, ya que no se han implementado instrumentos para obtener esas magnitudes.

## 2. Mapa de dependencias

**Optimización de escritura:**

Estrategia B → menor cantidad de operaciones de apertura y cierre → menor trabajo de entrada y salida → posible disminución del tiempo de ejecución (s).

**Optimización de lectura:**

Estrategia C → menor cantidad de operaciones de lectura → menor trabajo de entrada y salida → posible disminución del tiempo de ejecución (s) y aumento de la tasa de transferencia (MB/s).

**Tamaño de entrada:**

Cantidad de eventos (n) → cantidad de datos procesados → tiempo de ejecución (s) y tasa de transferencia (MB/s).

## 3. Variables que NO controlamos y cómo las mitigamos

| Variable no controlada | Efecto posible | Mitigación |
|---|---|---|
| Frecuencia dinámica del procesador | Puede modificar la velocidad de ejecución. | Mantener condiciones de alimentación similares y registrar el equipo utilizado. |
| Procesos del sistema operativo | Pueden consumir recursos y aumentar el tiempo de ejecución. | Cerrar programas innecesarios antes de realizar las pruebas. |
| Caché de archivos del sistema operativo | Puede hacer que las lecturas sean más rápidas al utilizar datos almacenados en RAM. | Mantener y documentar la misma condición de lectura en las comparaciones. |
| Diferencias entre computadores | Pueden producir tiempos distintos entre integrantes. | Comparar cada estrategia con su línea base ejecutada en el mismo computador. |

## 4. Consideraciones experimentales

Cada integrante registrará las características de su computador y las condiciones en las que realiza las pruebas.

Las comparaciones se realizarán utilizando los mismos datos de entrada y las mismas condiciones de ejecución. Cuando se comparen resultados de diferentes computadores, se analizará el porcentaje de mejora respecto a la línea base de cada equipo.

La tasa de transferencia se calculará dividiendo la cantidad de bytes procesados entre el tiempo de ejecución, utilizando MB decimales.