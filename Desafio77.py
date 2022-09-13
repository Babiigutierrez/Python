print('-'*34)
print('     \33[1mIdentificando as Vogais')
print('-'*34)
Palavras = ('Agua', 'carro', 'amor', 'borracha', 'lapis', 'acento', 'onibus',
            'computador', 'programaçao','promoçao', 'aviao', 'caminhao',
            'elefante', 'mamifero', 'onipresente')
for p in Palavras:
    print(f'\nNa palavra \33[1m{p.upper()}\33[m temos', end= ' ')
    for letra in p:
        if letra in 'AaEeIiOoUu':
            print(f'{letra}', end= ' ')