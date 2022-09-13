Números = []
while True:
    Núm = int(input('Digite um número:'))
    if Núm not in Números:
        Números.append(Núm)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor duplicado! Não irei adicionar...')
    r = ''
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'N':
        break
        print('Vou um prazer trabalhar com você. Volte sempre!')
Lista = Números
Números.sort()
print('-=' * 22)
print(f'Você digitou os valores {Lista}')