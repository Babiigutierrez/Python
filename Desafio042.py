print('-=-' *20)
print('Analisando triângulos')
print('-=-' *20)
Reta1 = float(input('Primeiro segmento:'))
Reta2 = float(input('Segundo segmento:'))
Reta3 = float(input('Terceiro segmento:'))
if (Reta1 + Reta2 > Reta3) or (Reta1 + Reta3 > Reta2) or (Reta3 + Reta2 > Reta1):
    print(f'As retas {Reta1},{Reta2} e {Reta3} PODEM formar um triângulo.' , end ='')
    if Reta1 == Reta2 == Reta3:
        print(f'Formam um triângulo EQUILÁTERO.')
    elif (Reta1 != Reta2) and (Reta1 != Reta3) and (Reta2 != Reta3):
        print(f'Formam um triângulo ESCALENO.')
    else:
        print(f'Formam um triângulo ISÓCELES.')
else:
    print(f'As retas {Reta1}, {Reta2} e {Reta3} NÃO PODEM formar um triângulo')