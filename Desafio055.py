Lista = []
for c in range (1,5+1):
    Peso = float(input(f'Informe o {c}ª peso:Kg'))
    Lista += [Peso]
print(f'''Maior peso: {max(Lista)}
Menor peso: {min(Lista)}''')