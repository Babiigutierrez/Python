Nome = str(input('Qual é o seu nome?')).strip().capitalize()
Nota1 = float(input('Primeira nota:'))
Nota2 = float(input('Segunda nota:'))
Média = (Nota1 + Nota2)/2
print(f'{Nome}, sua média foi {Média :.1f}')
if Média < 5:
    print(f'{Nome}, você está \33[1;31mREPROVADO\33[m! Estude mais no ano que vem.')
elif 5 <= Média <= 6.9:
    print(f'{Nome},você está de \33[1;33mRECUPERAÇÃO\33[m.')
else:
    print(f'PARABÉNS {Nome}!Você está \33[1;32mAPROVADA\33[m!')