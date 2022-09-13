from random import randint
from time import sleep
from operator import itemgetter
print('-='*25)
print('                   JOGO DE DADOS')
print('-='*25)
Jogo = {}
Ranking = ()
QtdJogador = int(input('Quantos jogadores participarão do jogo?'))
TotJogador = 1
while TotJogador <= QtdJogador:
    for c in range(1,QtdJogador+1):
        Jogo[f'Jogador {c}'] = randint(1,6)
        TotJogador += 1
    print('='*50)
for k,v in Jogo.items():
    print(f'{k} tirou {v} no dado')
    sleep(1)
print('='*50)
print('              RANKING DOS  VENCEDORES')
print('='*50)
Ranking = sorted(Jogo.items(), key = itemgetter(1), reverse=True)
for i,v in enumerate(Ranking):
    print(f'{i+1}ª: {v[0]} com {v[1]} pontos')
    sleep(1)