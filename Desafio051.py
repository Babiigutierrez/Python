print('-=' *7)
print('\33[1mCálculo da PA\33[m')
print('-=' *7)
NúmeroInicial = int(input('Primeiro Termo:'))
Razão = int(input('Razão:'))
N = int(input('Quantos elementos exibir:'))
NúmeroFinal = NúmeroInicial + (N-1)*Razão
print(f'''Cálculo da PA:
Primeiro Termo:{NúmeroInicial}
Razão:{Razão}
Os 10 primeiros termos dessa PA são:''')
for c in range (NúmeroInicial,NúmeroFinal+1,Razão):
    print(c, end='->')
print('ACABOU')