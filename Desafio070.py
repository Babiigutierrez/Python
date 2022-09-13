Total = ContPreço = MenorPreço = ContMenorPreço = 0
print('      MERCADO GUTIERREZ             ')
Barato = ' '
while True:
    print('-' *28)
    Nome = str(input('Qual é o produto?'))
    Preço = float(input('Quanto custa? R$'))
    ContMenorPreço += 1
    print('-' *28)
    Total += Preço
    if Preço > 1000:
        ContPreço +=1
    if ContMenorPreço == 1:
        MenorPreço = Preço
        Barato = Nome
    else:
        if Preço < MenorPreço:
            MenorPreço = Preço
            Barato = Nome
    Desejo = ' '
    while Desejo not in 'SN':
        Desejo = str(input('Você deseja continuar? [S/N]')).strip().capitalize()[0]
    if Desejo == 'N':
        break
print(f'''O preço total das compras foi R${Total :.2f}.
{ContPreço} produtos custaram mais que R$1000,00.
O produto mais barato foi {Barato} e custou R${MenorPreço :.2f}.
Muito bom receber você aqui.
Muito obrigada pela preferência e volte sempre! ''')