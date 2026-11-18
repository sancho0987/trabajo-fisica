"""Punto de entrada: python -m experimentos.ejecutar_experimento"""
import argparse
from src.configuracion import TAMANOS, REPETICIONES, TRABAJADORES, ESTRATEGIAS
from src.estrategias import estrategia_secuencial, estrategia_hilos, estrategia_procesos
from src.medicion import medir
from src.almacenamiento import guardar_resultados
from src.entorno import guardar_entorno

FUNCIONES = {
    "secuencial": estrategia_secuencial,
    "hilos": estrategia_hilos,
    "procesos": estrategia_procesos,
}

def ejecutar(tamanos=TAMANOS, repeticiones=REPETICIONES, estrategias=ESTRATEGIAS,
             trabajadores=TRABAJADORES, carpeta="resultados"):
    registros = []
    for tamano in tamanos:
        referencia = estrategia_secuencial(tamano)
        for nombre in estrategias:
            funcion = FUNCIONES[nombre]
            for repeticion in range(1, repeticiones + 1):
                if nombre == "secuencial":
                    resultado, duracion = medir(funcion, tamano)
                else:
                    resultado, duracion = medir(funcion, tamano, trabajadores)
                if resultado != referencia:
                    raise AssertionError(
                        f"{nombre} produjo {resultado}, se esperaba {referencia} para N={tamano}"
                    )
                registros.append({
                    "tamano": tamano,
                    "estrategia": nombre,
                    "repeticion": repeticion,
                    "resultado": resultado,
                    "tiempo_segundos": round(duracion, 8),
                })
                print(f"N={tamano:>7} | {nombre:<10} | repetición {repeticion}/{repeticiones} "
                      f"| primos={resultado} | {duracion:.6f} s")
    guardar_resultados(registros, carpeta)
    guardar_entorno(f"{carpeta}/entorno.json")
    print(f"\nExperimento terminado. Archivos guardados en: {carpeta}/")
    return registros

def main():
    parser = argparse.ArgumentParser(description="Compara ejecución secuencial, con hilos y procesos.")
    parser.add_argument("--repeticiones", type=int, default=REPETICIONES)
    parser.add_argument("--tamanos", type=int, nargs="+", default=TAMANOS)
    parser.add_argument("--trabajadores", type=int, default=TRABAJADORES)
    parser.add_argument("--rapido", action="store_true")
    args = parser.parse_args()
    if args.repeticiones < 5:
        parser.error("Se requieren mínimo 5 repeticiones por caso.")
    if any(n < 0 for n in args.tamanos):
        parser.error("Los tamaños deben ser números no negativos.")
    if args.rapido:
        ejecutar([100], 1, ESTRATEGIAS, args.trabajadores, "resultados_rapidos")
    else:
        ejecutar(args.tamanos, args.repeticiones, ESTRATEGIAS, args.trabajadores)

if __name__ == "__main__":
    main()
