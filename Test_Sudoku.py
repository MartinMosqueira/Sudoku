import unittest
from sudoku import sudoku

class Test_Sudoku(unittest.TestCase):

    def test_sudoku_isover(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        game.mostar()
        self.assertTrue(game)

    def test_ingresar_1(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79').ingresar(1, 3)
        self.assertTrue(game)

    def test_ingresar_2(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79').ingresar(0, 2)
        self.assertFalse(game)

    def test_verificar_valores_1(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79').verificar_valores(0,2 )
        self.assertFalse(game)


if __name__ == '__main__':
    unittest.main()