soma = 0
contador = 0
for c in  range (1,6+1):
    Num=int(input(f'Digite o {c} número:'))
    if Num % 2 ==0:
        soma +=Num
        contador += 1
print(f'Soma dos {contador} números pares foi {soma}')