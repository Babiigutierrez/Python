Matriz =[[0,0,0], [0,0,0], [0,0,0]]
SomaPar = MaiorValor = SomaColuna = 0
for Linha in range(0,3):
    for Coluna in range(0,3):
        Matriz[Linha][Coluna]= int(input(f'Digite um número para [{Linha},{Coluna}]:'))
print('-='*30)
for Linha in range(0,3):
    for Coluna in range(0,3):
        print(f'{Matriz[Linha][Coluna]:^5}', end='')
        if Matriz[Linha][Coluna] % 2 == 0:
            SomaPar += Matriz[Linha][Coluna]
    print()
print('-='*30)
print(f'A soma dos pares existentes na matriz é {SomaPar}')
for Linha in range(0,3):
    SomaColuna += Matriz[Linha][2]
print('-='*30)
print(f'A soma dos valores da terceira coluna é {SomaColuna}')
for Coluna in range(0,3):
    if Coluna == 0:
        MaiorValor = Coluna
    elif Matriz[1][Coluna] > MaiorValor:
            MaiorValor = Matriz[1][Coluna]
print('-='*30)
print(f'O maior valor da segunda linha é {MaiorValor}')
