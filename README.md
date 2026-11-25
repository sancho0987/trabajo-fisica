# Experimento de lectura y escritura de archivos

Experimento reproducible para el caso simulado de DocuArchivo S.A.S. Compara una línea base que abre/cierra el archivo por evento y lo lee byte a byte con dos tamaños de bloque y una alternativa de texto por líneas. Todas las estrategias procesan registros idénticos; su longitud y SHA-256 se verifican en cada medición.

## Requisitos

- Python 3.10 o superior.
- No requiere paquetes externos.

## Primera evidencia

Desde la raíz del repositorio:

```bash
python -m src.linea_base
```

La ejecución predeterminada procesa 5.000 eventos de 64 bytes e imprime tiempo, bytes y SHA-256; guarda la evidencia en `resultados/evidencia_linea_base.json`.

## Verificación y experimento

```bash
python -m unittest discover -s pruebas -v
python -m experimentos.ejecutar_experimento
```

El experimento usa cinco repeticiones y tamaños de escritura de 4 KiB y 64 KiB. Para cambiar parámetros:

```bash
python -m experimentos.ejecutar_experimento --eventos 20000 --bytes-por-evento 64 --repeticiones 7 --bloques 4096 65536 262144
```

Las repeticiones no pueden ser inferiores a cinco. Se generan `resultados.csv`, `resultados.json`, `entorno.json`, `resumen.json` y `comparacion.svg` en la carpeta de resultados.

## Diseño y análisis

El procedimiento, las variables, la hipótesis, la explicación de latencia/tasa y las limitaciones de caché están en [docs/protocolo.md](docs/protocolo.md). La lectura puede servirse desde RAM por la caché de páginas del sistema operativo; el informe no debe presentarla como una medición garantizada del disco físico.
