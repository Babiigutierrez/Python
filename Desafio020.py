from random import shuffle

Aluno1 = str(input('Primeiro aluno:'))
Aluno2 = str(input('Segundo aluno:'))
Aluno3 = str(input('Terceiro aluno:'))
Aluno4 = str(input('Quarto aluno:'))
Lista = [Aluno1, Aluno2, Aluno3, Aluno4]
shuffle(Lista)
print('A ordem de apresentação será')
print(Lista)
