# Protocolo experimental reproducible – Equipo 6

**Responsable:** Santiago Grajales (Integrante A)  
**Revisado por:** Todos los integrantes  
**Versión:** 1  
**Fecha:** 18/11/2026

## 1. Objetivo del experimento

Comparar el rendimiento de las estrategias de lectura y escritura de archivos mediante la medición del tiempo de ejecución y la tasa de transferencia de datos, utilizando la misma cantidad y contenido de eventos.

## 2. Preparación del entorno (antes de cada sesión)

1. Conectar el equipo a la corriente eléctrica y mantener un perfil de energía equilibrado.
2. Registrar las aplicaciones abiertas durante el experimento y cerrar aquellas que no sean necesarias.
3. Registrar las características del equipo utilizado, el sistema operativo y la versión de Python.
4. Ejecutar los programas utilizando la misma cantidad de eventos y la misma semilla de generación de datos.
5. Mantener las mismas condiciones de lectura en caliente para todas las estrategias.
6. Realizar las comparaciones en el mismo computador, para evitar que las diferencias entre equipos afecten los resultados.

## 3. Procedimiento

| Paso | Acción | Comando | Evidencia |
|---|---|---|---|
| 1 | Ejecutar la línea base | `py -m src.linea_base` | Resultado en terminal |
| 2 | Ejecutar la estrategia B | `py -m src.estrategia_b` | Resultado y prueba de corrección |
| 3 | Ejecutar la estrategia C | py -m src.estrategia_c | Resultado y prueba de corrección |
| 4 | Comparar los resultados | Registro de las mediciones | Tabla comparativa |

Cada estrategia se ejecutará cinco veces para obtener mediciones que permitan comparar su rendimiento. Antes de registrar los resultados, se realizará una ejecución inicial de cada estrategia.

## 4. Parámetros

- **Tamaño de entrada:** 20.000 eventos. Justificación: corresponde a la cantidad utilizada en la medición de la línea base.
- **Repeticiones por estrategia:** 5 ejecuciones. Justificación: permite observar variaciones entre mediciones.
- **Calentamiento:** realizar una ejecución inicial de cada estrategia antes de registrar las cinco mediciones.
- **Orden:** alternar el orden de ejecución de las estrategias para reducir posibles efectos del orden de las pruebas.
- **Semilla:** 6, para mantener el mismo contenido de los eventos.

## 5. Criterios de calidad de los datos

- Se calculará el coeficiente de variación (CV) de los tiempos obtenidos para cada estrategia.
- Se buscará un CV igual o inferior al 10 %. Si se supera, se realizarán nuevas ejecuciones y se revisarán las condiciones del equipo.
- Los valores atípicos se identificarán mediante la regla de Tukey y se reportarán. Solo se excluirán cuando exista una causa documentada.
- Se comprobará que todas las estrategias procesen correctamente las 20.000 líneas y generen el mismo contenido y cantidad de bytes para garantizar una comparación justa.

## 6. Registro de incidentes

| Fecha/hora | Incidente | Corridas afectadas | Decisión |
|---|---|---|---|
| Durante las pruebas | Una primera medición de la línea base presentó una variabilidad superior al 10 % en el conjunto inicial. | Mediciones iniciales de A | Se realizaron cinco nuevas mediciones y se utilizaron como conjunto formal. |
| Durante las pruebas | La estrategia B generó inicialmente un archivo de tamaño diferente al de la línea base. | Primeras ejecuciones de B | Se corrigió el manejo de saltos de línea para garantizar archivos equivalentes y se repitieron las mediciones. |
| Durante las pruebas | La primera comprobación de corrección de la estrategia B no fue aprobada. | Primera ejecución de B | Se revisó y corrigió el cálculo de bytes esperados antes de realizar las mediciones válidas. |