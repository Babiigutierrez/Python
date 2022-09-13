Núm = Alternativas = Soma = 0
Núm = int(input('Digite um número:'))
while Núm != 999:
    Soma += Núm
    Alternativas += 1
    Núm = int(input('Digite um número:'))
print(f'''Foram digitados {Alternativas} números.
 A soma entre eles é {Soma}.
 FIM!''')