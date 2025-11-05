import unittest
from carpeta import carpeta
from mensaje import mensaje

class TestCarpeta(unittest.TestCase):
    def setUp(self):
        self.c = carpeta("Principal")
        self.m = mensaje("juan@gmail.com", "rodrigo@mail.com", "Informe", "Detalles de mes")
    
    def test_agregar_mensaje(self):
        self.c.agregar_mensaje(self.m)
        self.assertIn(self.m, self.c.mensajes)
    
    def test_mover_mensaje(self):
        sub = self.c.agregar_subcarpeta("Archivados")
        self.c.agregar_mensaje(self.m)
        self.assertTrue(self.c.mover_mensaje(self.m, sub))
        self.assertIn(self.m, sub.mensajes)
        self.assertNotIn(self.m, self.c.mensajes)

    def test_buscar_remitente(self):
        self.c.agregar_mensaje(self.m)
        resultados = self.c.buscar(remitente="juan")
        self.assertIn(self.m, resultados)

if __name__ == "__main__":
    unittest.main()