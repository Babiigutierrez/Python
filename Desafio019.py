from random import choice
Aluno1 = str(input('Digite o nome do primeiro aluno:'))
Aluno2 = str(input('Digite o nome do segundo aluno:'))
Aluno3 = str(input('Digite o nome do terceiro aluno:'))
Aluno4 = str(input('Digite o nome do quarto aluno:'))
Lista = [Aluno1,Aluno2,Aluno3,Aluno4]
print(f'O aluno escolhido foi {choice(Lista)}')
