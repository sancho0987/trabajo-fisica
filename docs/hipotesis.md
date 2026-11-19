# Hipótesis del equipo – Equipo 6

Una hipótesis verificable permite anticipar un cambio medible en el rendimiento del programa y comprobar si la predicción se cumple mediante experimentos.

## H1. Optimización del proceso de escritura

**Hipótesis completa:**

Si se mantiene abierto el archivo durante todo el proceso de escritura, en lugar de abrirlo y cerrarlo por cada evento, entonces el tiempo total de ejecución (s) disminuirá al menos un 20 % respecto a la línea base, porque se reducirán las operaciones de apertura y cierre del archivo y el trabajo adicional que estas generan, manteniendo constantes la cantidad y el contenido de los eventos, el equipo y las condiciones de ejecución.

- **VI:** método de escritura del archivo.
- **VD:** tiempo total de ejecución (s).
- **Predicción cuantitativa:** reducción mínima del 20 %. Tomando como referencia 3,738 s, el tiempo esperado es de aproximadamente 2,99 s o menos.
- **Mecanismo físico/computacional:** reducir las operaciones de apertura y cierre del archivo disminuye el trabajo de entrada y salida y puede reducir el tiempo de ejecución.
- **¿Cómo la refutaríamos?:** si las mediciones repetidas muestran que la reducción del tiempo es inferior al 20 % o que el tiempo aumenta.

**Resultado experimental:** Cumplida. La estrategia B obtuvo un tiempo promedio aproximado de 0,092 s, equivalente a una reducción del 97,54 % respecto a la línea base.

## H2. Optimización del proceso de lectura

**Hipótesis completa:**

Si se realiza la lectura del archivo por bloques de 8.192 bytes, en lugar de leer un byte por operación, entonces el tiempo total de ejecución (s) disminuirá al menos un 10 % respecto a la línea base, porque se reducirá la cantidad de operaciones de lectura y el tiempo asociado a ellas, manteniendo constantes la cantidad y el contenido de los eventos, el equipo y las condiciones de ejecución.

- **VI:** método y tamaño del bloque de lectura.
- **VD:** tiempo total de ejecución (s).
- **Predicción cuantitativa:** reducción mínima del 10 %. Tomando como referencia 3,738 s, el tiempo esperado es de aproximadamente 3,36 s o menos.
- **Mecanismo físico/computacional:** leer varios bytes en una sola operación disminuye la cantidad de solicitudes de lectura y puede mejorar la tasa de transferencia de datos (MB/s).
- **¿Cómo la refutaríamos?:** si las mediciones repetidas muestran que la reducción del tiempo es inferior al 10 % o que el tiempo aumenta.

**Resultado experimental:** Refutada. La estrategia C obtuvo un tiempo promedio de 3,866 s, aproximadamente un 3,42 % mayor que la línea base. No se alcanzó la reducción esperada.

## Tabla resumen de hipótesis

| Id | VI | VD (unidad) | Predicción cuantitativa | Resultado |
|---|---|---|---|---|
| H1 | Método de escritura | Tiempo (s) | Disminución ≥ 20 % | Cumplida |
| H2 | Método de lectura | Tiempo (s) | Disminución ≥ 10 % | Refutada |

## Condiciones experimentales

Para comprobar las hipótesis se utilizaron los mismos 20.000 eventos, la misma semilla de generación de datos y el mismo contenido del archivo.

Las comparaciones se realizaron en el mismo computador, registrando sus características y procurando mantener las mismas condiciones de ejecución y el mismo estado de caché.

Los resultados corresponden al promedio de cinco mediciones válidas por estrategia. Todas cumplieron el criterio de coeficiente de variación inferior al 10 %.

No se afirmará una reducción del consumo de energía, ya que esta magnitud no se está midiendo directamente.