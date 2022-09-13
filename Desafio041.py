Nome = str(input('Qual é seu nome?'))
AnodeNascimento = int(input('Qual ano você nasceu?'))
Idade = 2022 - AnodeNascimento
if Idade <= 9:
    print(f'Boa sorte, {Nome}! Como você tem {Idade} anos, competirá na categoria MIRIM.')
elif Idade <= 14:
    print(f'Boa sorte, {Nome}! Como você tem {Idade} anos, competirá na categoria INFANTIL.')
elif Idade <= 19:
    print(f'Boa sorte, {Nome}! Como você tem {Idade} anos, competirá na categoria JÚNIOR.')
elif Idade<= 25:
    print(f'Boa sorte, {Nome}! Como você tem {Idade} anos, competirá na categoria SÊNIOR.')
else:
    print(f'Boa sorte, {Nome}! Como você tem {Idade} anos, competirá na categoria MASTER.')