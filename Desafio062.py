print('-=' *7)
print('\33[1mCálculo da PA\33[m')
print('-=' *7)
NúmInicial = int(input('Primeiro Termo:'))
Razão = int(input('Razão da P.A:'))
NúmFinal = NúmInicial
c = 1
total = 0
N = 10
while N != 0:
    total += N
    while c <= total:
        print(f'{NúmFinal}', end='->')
        NúmFinal += Razão
        c +=1
    print('PAUSA')
    N = int(input('Quantos termos você quer mostrar a mais?'))
print('Fim')

