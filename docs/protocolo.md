# Protocolo experimental: auditoría de archivos

## Objetivo

Comparar el costo de generar y volver a leer un registro de auditoría digital con distintas estrategias de E/S. Todas procesan los mismos eventos y deben producir exactamente los mismos bytes (longitud y SHA-256).

## Hipótesis

La línea base realizará más llamadas de apertura y lectura que las alternativas, por lo que se espera que tarde más. Agrupar escrituras reduce llamadas pequeñas y la lectura por bloques reduce iteraciones; el modo texto por líneas puede ser cómodo, aunque su decodificación tiene un costo adicional.

## Estrategias

| Identificador | Escritura | Lectura |
| --- | --- | --- |
| `linea_base` | Abre y cierra el archivo por cada evento | Lee byte a byte |
| `buffer_4096` | Archivo abierto; acumula bloques de 4 KiB | Lee bloques de 64 KiB |
| `buffer_65536` | Archivo abierto; acumula bloques de 64 KiB | Lee bloques de 64 KiB |
| `texto_lineas` | Archivo abierto en modo texto | Itera línea por línea |

## Variables

- **Independientes:** estrategia de E/S, número de eventos y tamaño del bloque de escritura.
- **Dependientes:** tiempo de pared, tiempo de CPU y tasa de transferencia en MiB/s.
- **Controladas:** equipo, unidad y sistema de archivos, contenido, tamaño de cada registro, versión de Python, aplicaciones abiertas y ubicación temporal de los archivos.

## Procedimiento

1. Registrar primero la línea base: `python -m src.linea_base`. Su resultado queda en `resultados/evidencia_linea_base.json`.
2. Ejecutar la verificación de contenido: `python -m unittest discover -s pruebas -v`.
3. Ejecutar la comparación: `python -m experimentos.ejecutar_experimento`.
4. Revisar CSV, JSON, resumen estadístico y gráfico SVG en `resultados/`.
5. Repetir en el mismo equipo; no usar el computador durante las mediciones y cerrar aplicaciones intensivas.

El valor por defecto es 5.000 eventos de 64 bytes y cinco repeticiones por estrategia. Se usa un archivo temporal nuevo para cada repetición. El tiempo medido incluye escritura, cierre y lectura, pero no la creación del directorio ni la exportación de resultados. Se informa la mediana, la media y la desviación estándar.

## Interpretación física y límites

La tasa se calcula como `R = D/t`, con `D` en MiB y `t` en segundos. Abrir/cerrar y leer byte a byte aumenta el trabajo por operación: cada llamada tiene un costo fijo en el sistema operativo y en el programa. La agrupación en búfer amortiza ese costo.

En un HDD, el movimiento mecánico y los desplazamientos del cabezal pueden dominar accesos físicos dispersos; en un SSD, las celdas flash no tienen partes móviles y la latencia suele ser menor. Este experimento usa acceso secuencial y no compara dispositivos distintos, así que no permite atribuir causalmente diferencias a HDD frente a SSD.

El sistema operativo puede servir lecturas desde su caché de páginas; por eso las mediciones no representan necesariamente lecturas físicas del disco. No se vacía la caché porque eso exige privilegios y altera el entorno. Los resultados describen este equipo, archivo y estado de caché; comparar medianas y dispersión es más informativo que una ejecución aislada.

## Resultados observados en la ejecución de referencia

Con 5.000 eventos de 64 bytes, la primera evidencia de línea base tardó 1,427 s (0,214 MiB/s). En la corrida comparativa final de cinco repeticiones, las medianas fueron: línea base 1,382 s; bloque de 4 KiB 0,026 s; bloque de 64 KiB 0,028 s; texto por líneas 0,026 s. Las alternativas generaron los mismos 320.000 bytes y el mismo SHA-256. En esta ejecución, el bloque de 4 KiB fue apenas más rápido que texto por líneas y su mediana fue aproximadamente 53 veces menor que la base. Es un resultado local con caché no controlada, no una conclusión general sobre todos los discos o tamaños.

## Bitácora

Registrar aquí fecha, integrantes, equipo, cambios al protocolo y observaciones relevantes de cada ejecución. El programa guarda metadatos de sistema y Python en `resultados/entorno.json`.
