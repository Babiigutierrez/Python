print('-='*4)
print('\33[1mTabuada\33[m')
print('-='*4)
Número = int(input('Insira um número:'))
print(f'\33[1mTabuada do {Número}:\33[m')
Passo = Número
for c in range (Número,10+1):
    print(f'{Número} X {c} = {Número*c}' )