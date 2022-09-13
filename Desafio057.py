Sexo = str(input('Qual é o seu sexo?')).strip().upper()
while Sexo != 'F' and Sexo != 'M':
     Sexo = str(input('Dados inválidos.Pode repetir?')).strip().upper()
print(f'Sexo {Sexo} registrado com sucesso!')