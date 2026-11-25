"""Exportación de resultados a CSV y JSON."""
import csv
import json
from pathlib import Path

def guardar_resultados(registros, carpeta="resultados"):
    destino = Path(carpeta)
    destino.mkdir(parents=True, exist_ok=True)
    campos = ["tamano", "estrategia", "repeticion", "resultado", "tiempo_segundos"]
    with (destino / "resultados.csv").open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(registros)
    with (destino / "resultados.json").open("w", encoding="utf-8") as archivo:
        json.dump(registros, archivo, ensure_ascii=False, indent=2)
