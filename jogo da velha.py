from funções import clear,exibir,bot,win

tabuleiro = [[' ',' ',' '],
             [' ',' ',' '],
             [' ',' ',' ']]

exibir(tabuleiro)



while True:
    linha = int(input('Informe a linha: '))-1
    coluna = int(input('Informe a coluna'))-1
    clear()

    if linha <= 3 and coluna <=3:
        if tabuleiro[linha][coluna]  != 'X' and  tabuleiro[linha][coluna] != 'O': 
            tabuleiro[linha][coluna] = 'X'

            bot(tab = tabuleiro)
            exibir(tabuleiro)

            if win(tab= tabuleiro):
                print(win(tabuleiro))
                break
               


        else: 
            print('Já existe um caractere nessa linha/coluna')
            
    else: 
        print('\nFora do intervalo')

    
    