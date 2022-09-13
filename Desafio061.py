print('-=' *7)
print('\33[1mCálculo da PA\33[m')
print('-=' *7)
NúmeroInicial = int(input('Primeiro Termo:'))
Razão = int(input('Razão:'))
N = int(input('Quantos elementos exibir:'))
NúmeroFinal = NúmeroInicial
cont = 1
while cont <= N:
    print(f'{NúmeroFinal}', end='->')
    NúmeroFinal += Razão
    cont +=1
print('FIM')