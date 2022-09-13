print('-='*16)
print('\33[1mNúmeros Impares e Mútiplos de 3\33[m')
print('-=' *16)
soma = 0
cont = 0
for c in range (1,500+1,2):
    if c % 3 == 0:
        cont += 1
        soma += c
print(f'''Analisando o intervalo {1,500}:
A soma de todos os {cont} números solicitados é {soma}''')


