import unittest
from usuarios import usuarios
from mensaje import mensaje

class TestUsuarios(unittest.TestCase):
    def setUp(self):
        self.u = usuarios("Rodrigo", "clave123", "rodrigo@mail.com")
        self.m = mensaje("juan@mail.com", "rodrigo@mail.com", "Que onda", "Todo bien?")

    def test_datos_usuario(self):
        self.assertEqual(self.u.nombre, "Rodrigo")
        self.assertTrue(self.u.existente("clave123"))
        self.assertFalse(self.u.existente("otra"))

    def test_recibir_mensaje(self):
        self.u.recibir(self.m)
        self.assertIn(self.m, self.u.bandeja.mensajes)

    def test_listar(self):
        self.u.recibir(self.m)
        bandeja = self.u.listar()
        self.assertIn(self.m, bandeja.mensajes)

if __name__ == "__main__":
    unittest.main()