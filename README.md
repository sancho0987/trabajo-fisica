# Experimento: ejecución secuencial, hilos y procesos

Proyecto en Python que compara tres maneras de contar números primos desde 2 hasta N:
- **A (base):** ejecución secuencial.
- **B:** ejecución con hilos (`ThreadPoolExecutor`).
- **C:** ejecución con procesos (`ProcessPoolExecutor`).

Las tres estrategias deben devolver exactamente el mismo conteo. El experimento comprueba esta condición en cada caso y registra tiempos.

## Requisitos
- Python 3.10 o superior.
- No se necesitan paquetes externos para el experimento principal.
- `psutil` es opcional para el monitor.

## Instalación
Abre una terminal en la carpeta del proyecto y ejecuta:

```bash
python -m venv .venv
```

Windows:
```bash
.venv\Scripts\activate
```

macOS/Linux:
```bash
source .venv/bin/activate
```

Instalación opcional del monitor:
```bash
pip install -r requirements.txt
```

## Ejecutar pruebas
```bash
python -m unittest discover -s pruebas -v
```

## Ejecutar experimento
```bash
python -m experimentos.ejecutar_experimento
```

Por defecto usa tamaños 1000, 5000 y 10000 y realiza 5 repeticiones por cada estrategia y tamaño.

Personalizar:
```bash
python -m experimentos.ejecutar_experimento --tamanos 1000 5000 20000 --repeticiones 10 --trabajadores 4
```

Se exige un mínimo de 5 repeticiones.

## Resultados
Se crean automáticamente:
- `resultados/resultados.csv`
- `resultados/resultados.json`
- `resultados/entorno.json`

## Nota sobre Windows y procesos
Ejecuta el experimento como módulo desde la raíz del proyecto, usando el comando anterior. El punto de entrada protege la ejecución con `if __name__ == "__main__":`, y la función de trabajo está definida en el nivel superior de `src/estrategias.py`. Esto permite que Windows use el método `spawn` sin intentar importar código ejecutable del intérprete interactivo.

## Limitaciones de medición
Los procesos tienen un costo de creación y comunicación; en tamaños pequeños pueden ser más lentos. Los hilos pueden no acelerar cálculos intensivos en CPU en CPython debido al GIL. El rendimiento depende del hardware y del sistema operativo.
# Actualizacion de pruebas y sincronizacion
