"""Información reproducible del entorno de ejecución."""
import json
import platform
import sys
from pathlib import Path
import os

def guardar_entorno(ruta="resultados/entorno.json"):
    datos = {
        "sistema": platform.system(),
        "version_sistema": platform.version(),
        "arquitectura": platform.machine(),
        "procesador": platform.processor(),
        "python": sys.version,
        "cpu_logicas": os.cpu_count(),
    }
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    destino.write_text(json.dumps(datos, ensure_ascii=False, indent=2), encoding="utf-8")
    return datos
