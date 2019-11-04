from sudoku import sudoku
from colorama import Fore, Back, init

init()

class Interfaz():
    def __init__(self):
        self.interfaz = sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')

    def respuesta_ingresar(self, x, y, z):
        if self.interfaz.ingresar(x, y, z) == False:
            print(Fore.RED+'\nValores fuera de rango')
            input(Back.RESET+'Pulsa una tecla para continuar...\n')

    def respuesta_valores_Tablero(self, x, y):
        if self.interfaz.valores_tablero(x, y) == False:
            print(Fore.RED+'\nPosicion fija del tablero')
            input(Back.RESET+'Pulsa una tecla para continuar...\n')

    def respuesta_verificar_culumna_fila(self, x, y, z):
        if self.interfaz.verificar_columna_fila(x, y, z) == False:
            print(Fore.RED+'\nEl valor se encuentra en la fila o columna')
            input(Back.RESET+'Pulsa una tecla para continuar...\n')

    def respuesta_verificar_submatriz(self, x, y, z):
        if self.interfaz.verificar_submatriz(x, y, z) == False:
            print(Fore.RED+'\nPosicion dentro de submatriz')
            input(Back.RESET+'Pulsa una tecla para continuar...\n')

    def main_excepción_rango(self, x, y, z):

        try:
            self.respuesta_valores_Tablero(x, y)
            self.respuesta_verificar_culumna_fila(x, y, z)
            self.respuesta_verificar_submatriz(x, y, z)
            return True

        except IndexError:
            return False

    def main_run(self):

        while True:
            a = ''
            for i in range(9):
                for j in range(9):
                    a += str(self.interfaz.Tablero[j][i])+'\t'
                print(a)
                a = ''

            while True:
                try:
                    x = int(input('\nfila: '))
                    y = int(input('columna: '))
                    z = int(input('numero: '))
                    break

                except ValueError:
                    print(Fore.RED+'\nEl valor ingresado no es entero')
                    input(Back.RESET+'Pulsa una tecla para continuar...')

            if self.main_excepción_rango(x, y, z) == False:
                self.respuesta_ingresar(x, y, z)
            self.interfaz.run_sudoku(x, y, z)


            for i in range(9):
                for j in range(9):
                    if self.interfaz.Tablero[i][j] == 'x':
                        contador = +1
            if contador == 0:
                print('Gracias por jugar')
                break
            contador = 0

interfaz = Interfaz()
interfaz.main_run()