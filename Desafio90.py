print('='*30)
print('     APROVADO OU REPROVADO')
print('='*30)
Aluno = {}
QtdAluno = int(input('Quantos alunos tem na sala?'))
TotAluno = 1
while TotAluno <= QtdAluno:
    Aluno['NOME'] = str(input('Nome:')).strip().capitalize()
    Aluno['1ª Avaliação'] = float(input('1ª Avaliação:'))
    Aluno['2ª Avaliação'] = float(input('2ª Avaliação:'))
    Aluno['Média'] = (Aluno['1ª Avaliação'] +Aluno['2ª Avaliação'])/2
    TotAluno +=1
    if Aluno['Média'] >= 7:
        Aluno['Situação'] = 'APROVADO'
    elif 5 <= Aluno['Média'] < 7:
        Aluno['Situação'] = 'EM RECUPERAÇÃO'
    else:
        Aluno['Situação'] = 'REPROVADO'
    print('='*30)
    for k, v in Aluno.items():
        print(f'{k}: {v}')
