Num1 = float(input('Digite o primeiro valor:'))
Num2 = float(input('Digite o primeiro valor:'))
Num3 = float(input('Digite o primeiro valor:'))
# Verificando quem é o menor
menor = Num1
if Num2 < Num1 and Num2<Num3:
    menor = Num2
if Num3 < Num1 and Num3<Num2:
    menor = Num3
# Verificando quem é o maior
maior = Num1
if Num2>Num1 and Num2>Num3:
    maior = Num2
if Num3>Num1 and Num3>Num2:
    maior = Num3
print(f' Entre os números {Num1}, {Num2} e {Num3}:')
print(f'O maior valor: {maior}')
print(f'O menor valor: {menor}')

