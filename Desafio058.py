from random import randint
from time import sleep
tentativas = 1
computador = randint(0,10)
print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')
sleep(6)
Núm = int(input('Qual é o seu palpite?'))

while Núm != computador:
    if Núm < computador:
        Núm = int(input('''Mais... Tente mais uma vez.
        Qual é o seu palpite?'''))
    else:
        Núm = int(input('''Menos... Tente mais uma vez.
        Qual é o seu palpite?'''))
    tentativas += 1
print(f'Você venceu! Foram necessárias {tentativas} tentativas. O número escolhido foi {Núm}')
