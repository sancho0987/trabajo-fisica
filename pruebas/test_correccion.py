import tempfile
import unittest
from pathlib import Path

from src.estrategias import buffered, texto_lineas
from src.linea_base import ejecutar


class PruebasEstrategiasEIO(unittest.TestCase):
    def comparar(self, eventos, tamano):
        with tempfile.TemporaryDirectory() as carpeta:
            base = ejecutar(Path(carpeta) / "base.log", eventos, tamano)
            esperado = (base["bytes_leidos"], base["sha256"])
            for bloque in (1, 4096, 65536):
                with self.subTest(estrategia="buffer", bloque=bloque):
                    self.assertEqual(buffered(Path(carpeta) / f"b{bloque}.log", eventos, tamano, bloque), esperado)
            self.assertEqual(texto_lineas(Path(carpeta) / "texto.log", eventos, tamano), esperado)

    def test_estrategias_escriben_contenido_identico(self):
        self.comparar(7, 64)

    def test_archivos_vacios(self):
        self.comparar(0, 64)

    def test_rechaza_registro_demasiado_corto(self):
        with tempfile.TemporaryDirectory() as carpeta:
            with self.assertRaises(ValueError):
                buffered(Path(carpeta) / "error.log", 1, 4, 16)


if __name__ == "__main__":
    unittest.main()
