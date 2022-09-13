import random
print('-=-'*20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*20)
Número = random.randint(0,5)
Adivinha = int(input('Em que número eu pensei?'))
print('PROCESSANDO...')
if Adivinha != Número:
    print(f'GANHEI! Eu pensei no número {Número} e não no {Adivinha}')
else:
    print('PARABÉNS! Você conseguiu me vencer!')

