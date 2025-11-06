import unittest
from mensaje import mensaje

class TestMensaje(unittest.TestCase):
    def setUp(self):
        self.m = mensaje("juan@mail.com", "rodrigo@mail.com", "Informe", "Detalles del mes")

    def test_atributos(self):
        self.assertEqual(self.m.remitente, "juan@mail.com")
        self.assertEqual(self.m.destinatario, "rodrigo@mail.com")
        self.assertEqual(self.m.asunto, "Informe")
        self.assertEqual(self.m.cuerpo, "Detalles del mes")

if __name__ == "__main__":
    unittest.main()