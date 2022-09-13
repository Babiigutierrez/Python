Matriz =[[0,0,0], [0,0,0], [0,0,0]]
for Linha in range(0,3):
    for Coluna in range(0,3):
        Matriz[Linha][Coluna]= int(input(f'Digite um número para [{Linha},{Coluna}]:'))
print('-='*30)
for Linha in range(0,3):
    for Coluna in range(0,3):
        print(f'{Matriz[Linha][Coluna]:^5}', end='')
    print()

