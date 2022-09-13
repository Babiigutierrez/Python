totmenor = 0
totmaior = 0
for c in range (1,7+1):
    AnodeNascimento = int(input(f'Em que ano a {c}ª pessoa nasceu?'))
    Idade = 2022 - AnodeNascimento
    if Idade >= 21:
        totmaior += 1
    else:
        totmenor +=1
print(f'''Pessoas que  atingiram a maioridade: {totmaior}.
Pessoas que não atingiram a maioridade: {totmenor}''')