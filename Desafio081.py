Núm = []
while True:
    Núm.append(int(input('Digite um número:')))
    Resp = str(input('Quer continaur?[S/N]')).strip().upper()[0]
    if Resp == 'N':
        break
Núm.sort(reverse=True)
print('-='*30)
print(f'Foram digitados {len(Núm)} números.')
print('-='*30)
print(f'A lista na ordem decrescente: {Núm}')
print('-=' *30)
if Núm ==5:
    print('O 5 faz parte da lista.')
else:
    print('O 5 não faz parte da lista!.')