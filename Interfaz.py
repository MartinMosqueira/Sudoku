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

        x = input('\nfila: ')
        y = input('columna: ')
        z = input('numero: ')

        interfaz.run_sudoku(int(x), int(y), int(z))

        for i in range(9):
            for j in range(9):
                a += str(interfaz.Tablero[j][i])+'\t'
            print(a)
            a = ''


        for i in range(9):
            for j in range(9):
                if interfaz.Tablero[i][j] == 'x':
                    contador = +1
        if contador == 0:
            print('Gracias por jugar')
            break
main()