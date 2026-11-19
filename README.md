# Equipo 6 — Lectura y escritura de archivos

> Proyecto: *Laboratorio colaborativo de rendimiento y eficiencia computacional desde la física aplicada*
> Física Aplicada al Desarrollo de Software · SENA · ADSO · 7.º trimestre

## 1. Problema empresarial
**Empresa (caso simulado):** DocuArchivo S.A.S., custodia y auditoría de documentos digitales

El registro de auditoría ralentiza las transacciones y la generación del reporte diario tarda minutos en el servidor de archivos.

## 2. Situación inicial medible - Equipo 6

Se ejecutó el programa `src.linea_base.py` utilizando 20.000 eventos de auditoría y una semilla de generación de datos igual a 6.

Se realizaron cinco mediciones válidas, cuyos resultados fueron:

| Ejecución | Tiempo (s) | Tasa de transferencia (MB/s) |
|---|---:|---:|
| 1 | 3,66 | 0,25 |
| 2 | 3,72 | 0,25 |
| 3 | 3,77 | 0,25 |
| 4 | 3,80 | 0,25 |
| 5 | 3,74 | 0,25 |

**Resultados promedio:**

- Eventos procesados: 20.000.
- Líneas leídas: 20.000.
- Tamaño procesado: 0,93 MB.
- Tiempo promedio de ejecución: 3,738 segundos.
- Tasa de transferencia promedio: aproximadamente 0,25 MB/s.
- Coeficiente de variación: 1,42 %.

El procedimiento inicial realiza una apertura y cierre del archivo por cada evento registrado. Posteriormente, lee el archivo byte por byte para contar las líneas y los bytes.

La lectura se realizó inmediatamente después de la escritura, por lo que se considera una lectura en caliente, debido a la posible intervención de la caché de memoria RAM del sistema operativo.

Estos resultados constituyen la referencia inicial para comparar las estrategias de optimización.

## 3. Pregunta de investigación
¿Cómo cambia el tiempo total de ejecución (segundos) cuando se modifica el método de escritura y lectura de archivos, manteniendo constante la cantidad y el contenido de los eventos?

## 4. Hipótesis
Ver [docs/hipotesis.md](docs/hipotesis.md).

## 5. Estrategias
| Id | Estrategia | Idea principal | Efecto físico esperado | Responsable |
|---|---|---|---|---|
| A | Línea base | Abrir y cerrar el archivo por cada evento y leer byte por byte. | mayor tiempo por las operaciones repetidas de apertura, cierre y lectura. | R2 |
| B | Escritura Continua | Mantener el archivo abierto durante todo el proceso de escritura.| reducción del tiempo por mantener abierto el archivo. | R3 |
| C | Lectura por bloques | Leer varios bytes en una sola operación. | reducción de operaciones de lectura mediante bloques. | R3 |

La estrategia B cuenta con un primer prototipo implementado en src/estrategia_b.py. Su prueba de corrección fue aprobada.

Resultado inicial de la estrategia B:

Eventos procesados: 20.000.

Líneas leídas: 20.000.

Tamaño procesado: 0,93 MB.

Tiempo de ejecución: 0,092 segundos.

Tasa de transferencia: 10,09 MB/s.

Prueba de corrección: aprobada.

Esta medición es inicial y deberá verificarse mediante nuevas ejecuciones experimentales.

## 6. Cómo reproducir
```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requirements.txt                          # opcional: psutil, matplotlib
python -m src.linea_base                                 # situación inicial
python -m unittest discover -s pruebas                   # corrección
python -m experimentos.ejecutar_experimento              # experimento formal -> resultados/resultados.csv
python ruta/a/analizar_resultados.py resultados/resultados.csv
```

## 7. Integrantes y roles
| Rol | Integrante | Responsabilidad principal |
|---|---|---|
| R1 — Coordinación y protocolo experimental | Santiago Grajales | Mantiene el protocolo y la bitácora de decisiones; controla variables; modera issues y la planeación. |
| R2 — Desarrollo de estrategia base | Narly Sofia Quintero | Comprende y documenta la línea base; asegura la verificación de corrección (pruebas) de todas las estrategias. |
| R3 — Estrategias alternativas y optimización | David alejandro Rosales | Diseña e implementa las estrategias alternativas y justifica físicamente por qué deberían cambiar las magnitudes. |
| R4 — Automatización de mediciones y análisis | _(nombre)_ | Automatiza experimentos y registro CSV; produce estadísticas y gráficos; documenta el entorno. |

Los roles son flexibles: **todos** participan en la comprensión física y en el código.

## 8. Documentación
- [Variables](docs/variables.md) · [Protocolo](docs/protocolo.md) · [Entorno](docs/entorno.md)
- [Decisiones técnicas](docs/decisiones.md) · [Uso de IA](docs/uso_ia.md) · [Informe](docs/informe.md)

## 9. Resultados y conclusiones (Clase 5)

Se realizaron cinco mediciones válidas por estrategia, utilizando 20.000 eventos y archivos de aproximadamente 0.93 MB.

| Estrategia | Tiempo promedio (s) | CV (%) |
|---|---:|---:|
| A. Línea base | 3.738 | 1.42 |
| B. Escritura continua | 0.092 | 4.86 |
| C. Lectura por bloques | 3.866 | 3.45 |

### Conclusiones

- La estrategia B redujo aproximadamente un 97.54 % el tiempo de ejecución respecto a la línea base.
- La estrategia C presentó un tiempo aproximadamente un 3.42 % mayor que la línea base, por lo que no cumplió la reducción esperada.
- Las tres estrategias procesaron correctamente los 20.000 eventos.
- Todas las estrategias cumplieron el criterio de calidad establecido, con un coeficiente de variación inferior al 10 %.