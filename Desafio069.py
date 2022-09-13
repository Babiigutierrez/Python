ContIdade = ContHom = ContMul = 0
while True:
    print('-' *25)
    print('    CADASTRE UMA PESSOA')
    print('-' *25)
    Idade = int(input('Idade:'))
    Sexo = ' '
    while Sexo not in 'MF':
        Sexo = str(input('Sexo [M/F]:')).strip().upper()[0]
    if Idade > 18:
        ContIdade += 1
    if Sexo == 'M':
        ContHom += 1
    else:
        if Idade < 20:
            ContMul += 1
    Desejo = ' '
    print('-' * 25)
    while Desejo not in 'NS':
        Desejo= str(input('Você deseja continuar? [S/N]')).strip().upper()[0]
    if Desejo == 'N':
        break
print(f'''Analisando as pessoas cadastradas:
Total de pessoas com mais de 18 anos: {ContIdade}.
Ao todo temos {ContHom} homens cadastrados. 
Ao todo temos {ContMul} mulheres com menos de 20 anos.''')
print('''Foi um prazer ter você conosco!
Muito obrigada e volte sempre!''')
