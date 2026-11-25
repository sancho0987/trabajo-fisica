"""Monitor opcional. Requiere psutil; temperatura depende del sistema operativo."""
import csv
from pathlib import Path
from datetime import datetime

def tomar_muestra():
    try:
        import psutil
    except ImportError:
        raise RuntimeError("Instala psutil con: pip install psutil")
    frecuencia = psutil.cpu_freq()
    temperaturas = None
    try:
        sensores = psutil.sensors_temperatures()
        valores = [t.current for grupo in sensores.values() for t in grupo if t.current]
        temperaturas = max(valores) if valores else None
    except (AttributeError, OSError):
        pass
    return {
        "fecha_hora": datetime.now().isoformat(timespec="seconds"),
        "cpu_porcentaje": psutil.cpu_percent(interval=0.5),
        "frecuencia_mhz": frecuencia.current if frecuencia else None,
        "temperatura_c": temperaturas,
    }

def guardar_muestras(muestras, ruta="resultados/monitor.csv"):
    destino = Path(ruta)
    destino.parent.mkdir(parents=True, exist_ok=True)
    campos = ["fecha_hora", "cpu_porcentaje", "frecuencia_mhz", "temperatura_c"]
    with destino.open("w", newline="", encoding="utf-8") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=campos)
        escritor.writeheader()
        escritor.writerows(muestras)
