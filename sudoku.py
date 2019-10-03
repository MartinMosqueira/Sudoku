
class sudoku():

    def __init__(self, lista):
        fila = 9
        self.Tablero = [ [  lista[i+(j*9)]  for j in range(fila) ] for i in range(fila)]

    def ingresar(self, x, y):

        for i in range(1, 10):
            if x and y == i:
                return True

    def verificar_valores(self):

        for i in range(9):
            for j in range(9):
                if self.Tablero[i][j] != 'x':
                    self.almacen[i][j]
                else:
                    return False

    def mostar(self):
        print(self.Tablero)

s=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
s.verificar_valores(1,1)



