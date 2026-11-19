# Registro de decisiones técnicas (ADR breve)

## D-001 — Mantener condiciones equivalentes entre estrategias

- **Fecha:** 18/11/2026
- **Autor(es):** Equipo 6
- **Issue/PR:** No asociado.
- **Contexto:** Era necesario garantizar que las diferencias en los tiempos de ejecución se debieran a los cambios realizados en cada estrategia y no a diferencias en los datos procesados.
- **Opciones consideradas:**
  1. Ejecutar cada estrategia con archivos de diferente tamaño o contenido.
  2. Utilizar la misma cantidad de eventos, la misma semilla y el mismo contenido para todas las estrategias.
- **Decisión:** Mantener 20.000 eventos, semilla 6 y el mismo contenido y tamaño de archivo (0,93 MB) en las tres estrategias.
- **Justificación (incluya evidencia o principio físico):** Para que la comparación sea válida, se debe mantener constante la cantidad de información procesada. Así, los cambios en el tiempo de ejecución pueden relacionarse con las modificaciones en las operaciones de lectura y escritura.
- **Consecuencias / riesgos:** Se obtiene una comparación más justa entre las estrategias. Sin embargo, los resultados pueden variar en otros computadores o bajo condiciones de ejecución diferentes.