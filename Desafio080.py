Lista = []
for c in range (0,5):
    Núm = int(input('Digite um número:'))
    if c == 0 or Núm > Lista[len(Lista)-1]:
        Lista.append(Núm)
        print('Adicionado no final da lista...')
    else:
        Pos = 0
        while Pos < len(Lista):
            if Núm <= Lista[Pos]:
                Lista.insert(Pos, Núm)
                print(f'Adicionado na posição {Pos}')
                break
            Pos += 1
print('-='*31)
print(f'Os valores digitados em ordem crescente são {Lista}')

