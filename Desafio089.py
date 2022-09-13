print('-='*30)
print(                  'BOLETIM DA TURMA')
print('-='*30)
AlunoMédia = []
ALunoNota =[]
Boletim =[]
Média = []
TotalAlunos = 1
QuantALunos = float(input('Quantos alunos essa turma tem?'))
while TotalAlunos <= QuantALunos:
    nome = str(input('Nome:')).strip().capitalize()
    Nota1 = float(input('1ª Avaliação:'))
    Nota2 = float(input('2ª Avaliação:'))
    Média = (Nota1 + Nota2)/2
    TotalAlunos += 1
    AlunoMédia.append([nome, [Nota1,Nota2],Média])
AlunoMédia.sort()
print('Nº NOME             MÉDIA')
print('-='*30)
for i,a in enumerate(AlunoMédia):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
print('='*26y)
while True:
    print('-='*30)
    opção = int(input('Mostrar notas de qual aluno?[999 interrompe]'))
    if opção == 999:
        print('FINALIZANDO...')
        break
    if opção <= len(AlunoMédia)-1:
        print(f'Notas de {AlunoMédia[opção][0]} são {AlunoMédia[opção][1]}')




