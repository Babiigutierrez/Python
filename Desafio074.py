from random import randint
Núm = (randint(0,10), randint(0,10), randint(0,10), randint(0,10), randint(0,10))
print('Os números sorteados foram:')
for c in Núm:
    print(f'{c}', end= ' ')
print(f'''\nO maior número sorteado foi {max(Núm)}
O menor número sorteado foi: {min(Núm)}''')