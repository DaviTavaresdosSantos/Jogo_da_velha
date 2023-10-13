from random import randint
from os import system

def clear():
    system('clear')

def exibir(tab):
    for l in range(0,3):
        for c in range(0,3):
            print(tab[l][c], end = '/')
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
    if tab[0][0] and tab[1][1] and tab[2][2] == 'X':
        return '\nwin(x)\n'

