Núm = []
for c in range(0,5):
    Núm.append(int(input(f'Digite um número para a posição {c}:')))
Lista = Núm
print(f'''A Lista: {Lista}
O maior número foi {max(Lista)} nas {Lista.index(max(Lista))} posições 
O menor número foi {min(Lista)} nas {Lista.index(min(Lista))} posições.''')