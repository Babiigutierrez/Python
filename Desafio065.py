Resp = 'S'
Soma = Cont = Média = Maior = Menor = 0
while Resp == 'S':
    Núm = int(input('Digite um número:'))
    Soma += Núm
    Cont += 1
    if Cont ==1:
        Maior = Menor = Núm
    else:
        if Núm > Maior:
            Maior = Núm
        if Núm < Menor:
            Menor = Núm
    Resp = str(input('Você quer continuar [S/N]?')).strip().capitalize()[0]
Média = Soma/Cont
print(f'''Você digitou {Cont} números e a média desses valores digitados foi {Média}.
O menor número foi {Menor} e o maior número foi {Maior}.
FIM''')

