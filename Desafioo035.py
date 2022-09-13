print('-=-' *20)
print('Analisador de Triângulos')
print('-=-' *20)
Reta1 = float(input('Primeiro segmento:'))
Reta2 = float(input('Segundo segmento:'))
Reta3 = float(input('Terceiro segmento:'))
if  Reta1 + Reta2 > Reta3  and  Reta1 + Reta3 > Reta2  and  Reta2 + Reta3 > Reta1:
    print(f'As retas com dimensão {Reta1} X {Reta2} X {Reta3} formam um triângulo')
else:
    print(f'As retas com dimensão {Reta1} X {Reta2} X {Reta3} não formam um triângulo')
