Núm = Cont = Soma = 0
while True:
    Núm = int(input('Digite um número(O número 999 faz parar):'))
    if Núm == 999:
        break
    Cont += 1
    Soma += Núm
print(f'''Foram digitados {Cont} números.
A soma vale {Soma}.''')