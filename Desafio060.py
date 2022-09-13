Núm = int(input('''Digite um número para 
Calcular seu Fatorial:'''))
fatorial = Núm
resultado = Núm
while fatorial !=1:
    fatorial = fatorial - 1
    resultado = resultado * fatorial
print(f'O fatorial de {Núm} é {resultado}.')