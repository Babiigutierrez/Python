SomaIdade = 0
MediaIdade = 0
MaiorIdadeHomem = 0
NomeVelho = ''
MulherNova = 0
for c in range (1,5):
    print(f'----- {c}ª PESSOA -----')
    Nome  = str(input('Nome:')).strip().capitalize()
    Idade = int(input('Idade:'))
    Sexo  = str(input('Sexo [M/F]:')).strip().capitalize()
    SomaIdade += Idade
    if c == 1 and Sexo == 'M':
        MaiorIdadeHomem = Idade
        NomeVelho = Nome
    if Sexo == 'M' and Idade > MaiorIdadeHomem:
        MaiorIdadeHomem = Idade
        NomeVelho = Nome
    if Sexo =='F' and Idade < 20:
        MulherNova +=1

MediaIdade += SomaIdade/4
print(f'A média de idade do grupo é de {MediaIdade}')
print(f'O homem mais velho tem {MaiorIdadeHomem} anos e se chama {NomeVelho}')
print(f'Existem {MulherNova} mulheres com menos de 20 anos')