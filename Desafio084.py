Dados = []
Galera = []
MaiorPeso = MenorPeso = 0
while True:
    Dados.append(str(input('Nome:')))
    Dados.append(float(input('Peso:[KG] ')))
    if len(Galera) ==0:
        MaiorPeso = MenorPeso = Dados[1]
    else:
        if Dados[1] > MaiorPeso:
            MaiorPeso = Dados[1]
        if Dados[1] < MenorPeso:
            MenorPeso = Dados[1]
    Galera.append(Dados[:])
    Dados.clear()
    Resp = str(input('Deseja Continuar?[S/N]')).strip().upper()[0]
    if Resp == 'N':
        break
print('-='*30)
print(f'Os dados foram  {Galera}.')
print(f'Ao todo, você cadastrou {len(Galera)} pessoas.')
print(f'O maior peso é {MaiorPeso}Kg. Peso de ', end='')
for p in Galera:
    if p[1] == MaiorPeso:
        print(f'[{p[0]}]', end='')
print()
print(f'O menor peso é {MenorPeso}Kg. Peso de ', end='')
for p in Galera:
    if p[1] == MenorPeso:
        print(f'[{p[0]}]', end='')
