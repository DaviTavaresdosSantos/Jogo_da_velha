from random import randint
from os import system

def clear():
    system('clear')

def exibir(tab):
    for l in range(0,3):
        for c in range(0,3):
            print(tab[l][c], end = ' ')
        print()


def bot(tab):
    while True:
        linha = randint(0,2)
        coluna = randint(0,2)

        if tab[linha][coluna] == 'X' or tab[linha][coluna]== 'O':
            continue

        else:
            tab[linha][coluna] = 'O'
            break
            


def win(tab):
    if tab[0][0] == 'X' and tab[1][1] == 'X' and tab[2][2] == 'X':   #} vecer na diagonal(\)
        return 'Win(X)'

    elif tab[2][0] == 'X' and tab[1][1] == 'X' and tab[0][2] == 'X': #} vender na diagonal (/)
        return 'Win(X)'
    
    elif tab[0][0] == 'X' and tab[1][0] == 'X' and tab[2][0] == 'X': #} vencer em fila(---)
        return 'Win(X)' 

    elif tab[0][2] == 'X' and tab[1][2] == 'X' and tab[2][2] == 'X':#} vencer em fila(  |)
        return 'Win(X)'

    elif tab[1][0] == 'X' and tab[1][1] == 'X' and tab[1][2] == 'X': #} vencer em fima(meio(--))
        return 'Win(X)'

    elif tab[2][0] == 'X' and tab[2][1] == 'X' and tab[2][2] == 'X': #} vencer em fila(___)
        return 'Win(X)'

    elif tab[0][1] == 'X' and tab[1][1] == 'X' and tab[2][1] == 'X':
        return 'Win(X)'


    

    
