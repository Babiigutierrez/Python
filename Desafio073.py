TabelaBrasileirão2022 = ('Palmeiras', 'Corinthians', 'Internacional', 'Athletico-PR',
                        'São PAulo', 'Atlético-MG', 'Avaí', 'Santos', 'Bragantino',
                        'Flamengo', 'Fluminense', 'Coritiba', 'Amperica-MG', 'Botafogo',
                        'Ceará', 'Goiás', 'Atlético-GO', 'Cuiabá', 'Juventude', 'Fortaleza')
print('-='*15)
print(f'Lista de times do Brasileirão: {TabelaBrasileirão2022}')
print('-='*15)
print(f'Os 5 primeiros colocados do Brasileiro de 2022 são {TabelaBrasileirão2022[:5]}')
print('-='*15)
print(f'Os times que estão na zona de rebaixamento são {TabelaBrasileirão2022[-4:]}')
print('-='*15)
print(f'A ordem alfabética dos times: {sorted(TabelaBrasileirão2022)}')
print('-='*15)
print(f'O Flamengo está na {TabelaBrasileirão2022.index("Flamengo")+1}ª do Brasileirão')
print('-='*15)