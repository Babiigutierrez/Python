Velocidade = float(input('Qual é a velocidade atual do carro?'))
Multa = (Velocidade - 80)*7
if Velocidade > 80:
    print(f'MULTADO! Você ultrapassou o limite permitido que é de 80km/h\nVocê deve pagar uma multa de R${Multa :.1f}')
else:
    print('Parabés! Dirija com segurança.')
