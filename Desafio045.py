from random import randint
from time   import sleep
print('-=' *8)
print('\33[1mJogando Jokenpo\33[m')
print('-=' *8)
itens = ('Pedra','Papel','Tesoura')
computador = randint(0,2)
print(''' Suas opções: 
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada?'))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
print('-=' *12)
print(f'O computador jogou {itens[computador]}')
print(f'O jogador jogou {itens[jogador]}')
print('-=' *12)
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Jogador Venceu')
    elif jogador == 2:
        print('Computador Venceu')
    else:
        print('\33[31mJOGADA INVÁLIDA\33[m')
elif computador == 1:
    if jogador == 0:
        print('COMPUTADOR Venceu')
    elif jogador == 1:
        print('EMPATE')
    elif jogador == 2:
        print('JOGADOR Venceu')
    else:
        print('\33[31mJOGADA INVÁLIDA\33[m')
elif computador ==2:
    if jogador == 0:
        print('JOGADOR Venceu')
    elif jogador == 1:
        print('COMPUTADOR Venceu')
    elif jogador == 2:
        print('EMPATE')
    else:
        print('\33[31mJOGADA INVÁLIDA\33[m')
