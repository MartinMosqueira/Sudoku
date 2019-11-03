from sudoku import sudoku
from colorama import Fore, Back, init

interfaz=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')

init()

def respuesta_ingresar(x, y, z):
    if interfaz.ingresar(x, y, z) == False:
        print(Fore.RED+'\nValores fuera de rango')
        input(Back.RESET+'Pulsa una tecla para continuar...\n')

def respuesta_valores_Tablero(x, y):
    if interfaz.valores_tablero(x, y) == False:
        print(Fore.RED+'\nPosicion fija del tablero')
        input(Back.RESET+'Pulsa una tecla para continuar...\n')

def respuesta_verificar_culumna_fila(x, y, z):
    if interfaz.verificar_columna_fila(x, y, z) == False:
        print(Fore.RED+'\nEl valor se encuentra en la fila o columna')
        input(Back.RESET+'Pulsa una tecla para continuar...\n')

def respuesta_verificar_submatriz(x, y, z):
    if interfaz.verificar_submatriz(x, y, z) == False:
        print(Fore.RED+'\nPosicion dentro de submatriz')
        input(Back.RESET+'Pulsa una tecla para continuar...\n')



def main():

    while True:
        a = ''
        for i in range(9):
            if i == 3:
                print('\t')
            if i == 6:
                print('\t')
            for j in range(9):
                a += str(interfaz.Tablero[j][i])+'\t'
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
        try:
            respuesta_valores_Tablero(x, y)
            respuesta_verificar_culumna_fila(x, y, z)
            respuesta_verificar_submatriz(x, y, z)

        except IndexError:
            respuesta_ingresar(x, y, z)

        interfaz.run_sudoku(x, y, z)


        for i in range(9):
            for j in range(9):
                if interfaz.Tablero[i][j] == 'x':
                    contador = +1
        if contador == 0:
            print('Gracias por jugar')
            break
        contador = 0


main()

