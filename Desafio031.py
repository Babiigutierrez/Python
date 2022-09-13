Distância = float(input('Qual é a distância da sua viagem?'))
Custo = Distância*0.5 if Distância <= 200 else Distância*.45
print(f'Você está prestes a começar uma viagem de {Distância}Km.')
print(f'E o preço da sua passagem será de R${Custo :.2f}')