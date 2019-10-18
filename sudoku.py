
class sudoku():

    def __init__(self, lista):
        fila = 9
        self.Tablero = [ [  lista[i+(j*9)]  for j in range(fila) ] for i in range(fila)]
        self.valores_fijos = [ [  lista[i+(j*9)]  for j in range(fila) ] for i in range(fila)]

    def ingresar(self, x, y):
        if x and y <= 8 and x and y >= 0:
            return True
        else:
            return False

    #def valores_tablero(self):
        #self.valores_fijos = []
        #for i in range(9):
            #for j in range(9):
                #if self.Tablero[i][j] != 'x':
                    #self.valores_fijos.append(self.Tablero[i][j])
        #return self.valores_fijos

    def valores_tablero(self, x, y, z):
        if self.valores_fijos[x][y] == 'x':
            self.Tablero[x][y] = str(z)
        else:
            return False

    def verificar_columna_fila(self, x, y, z):
        for i in range(9):
            if self.Tablero[i][y] == str(z):
                return False
            if self.Tablero[x][i] == str(z):
                return False
            else:
                return True

    def verificar_submatriz(self, x, y, z):
        deff_x = (x//3)*3
        deff_y = (y//3)*3
        for i in range(3):
            for j in range(3):
                if self.Tablero[deff_x+i][deff_y+j] == str(z):
                    return False
        return True


    def mostar(self):
        print(self.Tablero)

s=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')
s.mostar()

