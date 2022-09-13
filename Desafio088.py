from  random import randint
print('-='*30)
print('                     JOGA NA MEGA SENA')
print('-='*30)
QuantJogos = int(input('Quantos jogos serão gerados?'))
TotalJogos = 0
Lista = []
Jogos = []
while TotalJogos <= QuantJogos:
    Cont =0
    while True:
        Núm = randint(1,60)
        if Núm not in Lista:
            Lista.append(Núm)
            Cont +=1
        if Cont >=6:
            break
    Lista.sort()
    Jogos.append(Lista[:])
    Lista.clear()
    TotalJogos +=1
print('-='*3,f' SORTEANDO {QuantJogos} JOGOS', '-='*3)
for i, l in enumerate(Jogos):
    print(f'Jogo {i+1}: {l}')
print('-='*30)
print('BOA SORTE!!!')