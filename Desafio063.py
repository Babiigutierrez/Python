print('-' *22)
print('Sequência de Fibonacci')
print('-' *22)
N = int(input('Quantos termos você quer mostrar?'))
Termo1 = 0
Termo2 = 1
print(f'{Termo1}->{Termo2}', end='->')
cont = 3
while cont <= N:
    Termo3 = Termo1 + Termo2
    print(f'{Termo3}', end= '->')
    Termo1 = Termo2
    Termo2= Termo3
    cont +=1
print('FIM')


