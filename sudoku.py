
class sudoku():

    def __init__(self, lista):
        fila = 9
        self.Tablero = [ [  lista[i+(j*9)]  for j in range(fila) ] for i in range(fila)]
        self.valores_fijos = [ [  lista[i+(j*9)]  for j in range(fila) ] for i in range(fila)]

    def mostar(self):
        print(self.Tablero)

    def ingresar(self, x, y):
        if x <= 8 and y <= 8:
            if x >= 0 and y >= 0:
                return True
            else:
                return False
        else:
            return False

    def valores_tablero(self, x, y):
        if self.valores_fijos[y][x] == 'x':
            return True
        else:
            return False

    def verificar_columna_fila(self, x, y, z):
        contador = 0
        for i in range(9):
            if self.Tablero[i][x] == str(z):
                contador=contador+1
            if self.Tablero[y][i] == str(z):
                contador=contador+1
        if contador == 0:
            return True
        else:
            return False

    def verificar_submatriz(self, x, y, z):
        contador = 0
        deff_x = (x//3)*3
        deff_y = (y//3)*3

        for i in range(3):
            if self.Tablero[deff_y][i+deff_x] == str(z):
                contador = contador + 1
            if self.Tablero[deff_y+1][i+deff_x] == str(z):
                contador = contador + 1
            if self.Tablero[deff_y+2][i+deff_x] == str(z):
                contador = contador + 1
        if contador == 0:
            return True
        else:
            return False

    def run_sudoku(self, x, y, z):

        if self.ingresar(x, y):
            if self.valores_tablero(x, y):
                if self.verificar_columna_fila(x, y, z):
                    if self.verificar_submatriz(x, y, z):
                        self.Tablero[y][x] = str(z)


s=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
#s=sudoku('531375555656195682195182163879868143483823461712527586165326283125419795895285794')
