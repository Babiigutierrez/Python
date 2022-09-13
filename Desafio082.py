Lista1 = []
ListaPar = []
ListaImpar = []
while True:
    Núm =int(input('Digite um número:'))
    if Núm % 2 == 0:
        ListaPar.append(Núm)
    else:
        ListaImpar.append(Núm)
    Lista1.append(Núm)
    Resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if Resp == 'N':
        break
print('-=' *30)
print(f'''A lista completa é {Lista1}
A lista dos pares é {ListaPar}
A lista dos impares é {ListaImpar} ''')