from sudoku import sudoku

interfaz=sudoku('53xx7xxxx6xx195xxxx98xxxx6x8xxx6xxx34xx8x3xx17xxx2xxx6x6xxxx28xxxx419xx5xxxx8xx79')

def main():

    while True:
        a = ''
        for i in range(9):
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
                print('El valor ingresado no es entero')

        interfaz.run_sudoku(x, y, z)

        if interfaz.ingresar(x, y) == False:
            print('\nValores fuera de rango')
            input('Pulsa una tecla para continuar...\n')

        if interfaz.ingresar(x, y) == True:
            if interfaz.valores_tablero(x, y) == False:
                print('\nPosicion fija del tablero')
                input('Pulsa una tecla para continuar...\n')

        #if interfaz.verificar_columna_fila(x,y,z)  == False:
            #print('\nEl valor se encuentra en la fila o columna')
            #input('Pulsa una tecla para continuar...\n')

        for i in range(9):
            for j in range(9):
                if interfaz.Tablero[i][j] == 'x':
                    contador = +1
        if contador == 0:
            print('Gracias por jugar')
            break
        contador = 0


main()