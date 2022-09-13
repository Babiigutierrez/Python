ListaMercado = ('Tomate', 8.50, 'Cebola', 5.00, 'Alho', 6.00, 'Pimentão', 9.00, 'Ovo', 20.00)
print('-'*33)
print('         Listagem de Preços')
print('-'*33)
for l in range (0, len(ListaMercado)):
    if l % 2 ==0:
        print(f'{ListaMercado[l] :.<30}', end= '')
    else:
        print(f'R${ListaMercado[l] :.2f}')
