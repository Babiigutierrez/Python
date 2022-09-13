Num = int(input('Digite um número entre 0 e 9999:'))
print(f'Analisando o número {Num}')
print(f'Unidade:{Num // 1 % 10}')
print(f'Dezena:{Num // 10 % 10}')
print(f'Centena:{Num // 100 % 10}')
print(f'Milhar:{Num // 1000 % 10}')



