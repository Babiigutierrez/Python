print('-=-' *20)
print('Calculadora de IMC')
print('-=-' *20)
Nome = str(input('Qual seu nome?')).strip().capitalize()
Peso = float(input('Qual seu peso? (kg)'))
Altura = float(input('Qual sua altura?'))
IMC =  Peso/(Altura*Altura)
if IMC < 18.5:
    print(f'{Nome}, seu IMC é {IMC :.2f} e você está ABAIXO DO PESO.')
elif 18.5 <= IMC < 25:
    print(f'{Nome}, seu IMC é {IMC :.2f} e você está com PESO IDEAL.')
elif 25 <= IMC < 30:
    print(f'{Nome}, seu IMC é {IMC :.2f} evocê está com SOBREPESO.')
elif 30 <= IMC < 40:
    print(f'{Nome}, seu IMC é {IMC :.2f} e você está com OBESIDADE.')
elif IMC >= 40:
    print(f'{Nome}, seu IMC é {IMC :.2f} e você está com OBESIDADE MÓRBIDA')
