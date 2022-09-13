Núm = [[],[]]
Valor = 0
for c in range(1,8):
    Valor = int(input(f'Digite o {c}ª número:'))
    if Valor % 2 == 0:
        Núm[0].append(Valor)
    else:
        Núm[1].append(Valor)
print('-='*30)
print(f'''Valores digitados: {Núm}
Valores pares digitados: {sorted(Núm[0])}
Valores ímpares digitados:{sorted(Núm[1])}''')