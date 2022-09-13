Nascimento = int(input('Em qual ano você nasceu?'))
Idade = 2022 - Nascimento
if Idade < 18:
    print(f'Você tem {Idade} anos, ainda não pode se alistar ao exército. Daqui {18-Idade} anos você poderá.')
elif Idade == 18:
    print(f'Se prepare! Você está com {Idade} anos. Estar na hora de se alistasr.')
else:
    print(f'Ainda não se alistou? Você tem {Idade} anos e passou {Idade - 18} anos do tempo para se alistar')
