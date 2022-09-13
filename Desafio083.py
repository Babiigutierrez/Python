Expre = str(input('Digite uma expressão:'))
Pilha = []
for símb in Expre:
    if símb == '(':
        Pilha.append('(')
    elif símb == ')':
        if len(Pilha) > 0:
            Pilha.pop()
        else:
            Pilha.append(')')
            break
if len(Pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está inválida!')

