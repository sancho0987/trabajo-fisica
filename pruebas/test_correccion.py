import unittest
from src.estrategias import estrategia_secuencial, estrategia_hilos, estrategia_procesos

class PruebasEstrategias(unittest.TestCase):
    def test_limites_pequenos(self):
        for limite in (0, 1, 2, 10, 100, 1000):
            esperado = estrategia_secuencial(limite)
            self.assertEqual(estrategia_hilos(limite, 2), esperado)
            self.assertEqual(estrategia_procesos(limite, 2), esperado)

    def test_valores_conocidos(self):
        # π(10)=4, π(100)=25, π(1000)=168
        self.assertEqual(estrategia_secuencial(10), 4)
        self.assertEqual(estrategia_secuencial(100), 25)
        self.assertEqual(estrategia_secuencial(1000), 168)

if __name__ == "__main__":
    unittest.main()
