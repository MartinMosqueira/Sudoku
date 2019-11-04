import unittest
from Interfaz import Interfaz

class Test_Interfaz_Sudoku(unittest.TestCase):

    def test_main_excepción_rango_1(self):
        respuesta = Interfaz().main_excepción_rango(4434, 9, 8)
        self.assertFalse(respuesta)

    def test_main_excepción_rango_2(self):
        respuesta= Interfaz().main_excepción_rango(0, 2, 2)
        self.assertTrue(respuesta)

    def test_main_excepción_rango_3(self):
        respuesta= Interfaz().main_excepción_rango(0, 45, 2)
        self.assertFalse(respuesta)

if __name__ == '__main__':
    unittest.main()