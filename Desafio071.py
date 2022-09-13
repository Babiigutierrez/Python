print('='*30)
print('          BANCO CEV')
print('='*30)
ContNota50 = ContNota20 = ContNota10 = ContNota1 = 0
Valor = int(input('Qual sera o valor do saque? R$'))
Total = Valor
Céd = 50
TotalCéd = 0
while True:
    if Total >= Céd:
        Total -= Céd
        TotalCéd +=1
    else:
        if TotalCéd >0:
            print(f'Total de {TotalCéd} cédulas de R${Céd}')
        if Céd == 50:
            Céd = 20
        elif Céd == 20:
            Céd =10
        elif Céd ==10:
            Céd =1
        TotalCéd = 0
        if Total == 0:
            break
print('='*30)
print('Volte sempre ao Banco CEV')



