Núm = (int(input('Digite um número:')), int(input('Digite um número:')),
int(input('Digite um número:')),int(input('Digite um número:')))

print(f'Você digitou os valores {Núm}')
print(f'O número 9 apareceu {Núm.count(9)} vezes.')
if 3 in Núm:
    print(f'O número 3 apareceu na {Núm.index(3)+1}ª posição.')
else:
    print('O valor 3 não vou digitado em nenhuma posição')
print('Os valores pares digitados são.', end= ' ')
for n in Núm:
    if n % 2 == 0:
        print(n, end= ' , ')
