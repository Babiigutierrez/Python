Casa = float(input('Qual o valor da casa?'))
Salário = float(input('Qual o seu salário?'))
Anos= float(input('Em quantos anos você irá pagar?'))
PrestaçãoMensal = Casa/(Anos*12)
if PrestaçãoMensal < (0.30*Salário):
    print(f'Para pagar uma casa de R${Casa} em {Anos} a prestação será de R${PrestaçãoMensal}.PARABÉNS!!! Empréstimo \33[1;32mAPROVADO\33[m.')
else:
    print(f'Para pagar uma casa de R${Casa} em {Anos} a prestação será de R${PrestaçãoMensal}. Empréstimo  \33[1;31mNEGADO\33[m!')