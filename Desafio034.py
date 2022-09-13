
Salário = float(input('Qual é o seu salário? R$'))
NovoSalário1 = Salário + (Salário*.15)
NovoSalário2 = Salário + (Salário*.10)
if Salário <= 1250.0:
    print(f'Quem ganhava {Salário} passará a ganhar R${NovoSalário1 :.2f}')
else:
    print(f'Quem ganhava {Salário} passará a ganhar R${NovoSalário2 :.2f}')

