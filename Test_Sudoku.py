import unittest
from sudoku import sudoku

class Test_Sudoku(unittest.TestCase):

    def test_sudoku_mostrar(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        game.mostar()
        self.assertTrue(game)

    def test_ingresar_1(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.ingresar(1, 3, 1)
        self.assertTrue(resultado)

    def test_ingresar_2(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.ingresar(0, 20, 8)
        self.assertFalse(resultado)

    def test_ingresar_3(self):
        game = sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.ingresar(-4, 8, 4)
        self.assertFalse(resultado)

    def test_valores_tablero_1(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.valores_tablero(0, 0)
        self.assertFalse(resultado)

    def test_valores_tablero_2(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.valores_tablero(4, 4)
        self.assertTrue(resultado)

    def test_valores_tablero_3(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.valores_tablero(8, 6)
        self.assertTrue(resultado)

    def test_verificar_columna_fila_1(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.verificar_columna_fila(0, 0, 5)
        self.assertFalse(resultado)

    def test_verificar_columna_fila_2(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.verificar_columna_fila(1, 1, 4)
        self.assertTrue(resultado)

    def test_verificar_columna_fila_3(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.verificar_columna_fila(3, 5, 4)
        self.assertTrue(resultado)

    def test_verificar_submatriz_1(self):
        game = sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.verificar_submatriz(7, 2, 6)
        self.assertFalse(resultado)

    def test_verificar_submatriz_2(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.verificar_submatriz(2, 4, 2)
        self.assertTrue(resultado)

    def test_verificar_submatriz_3(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.verificar_submatriz(5, 7, 5)
        self.assertTrue(resultado)

    def test_run_sudoku_1(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.run_sudoku(4, 4, 6)
        self.assertFalse(resultado)

    def test_run_sudoku_2(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.run_sudoku(8, 6, 9)
        self.assertFalse(resultado)

    def test_run_sudoku_3(self):
        game=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
        resultado = game.run_sudoku(8, 6, 4)
        self.assertFalse(resultado)

if __name__ == '__main__':
    unittest.main()