Nome = str(input('Digite seu nome completo: ')).strip()
print(f'Analisando seu nome...')
print(f'Seu nome em maiúscula é {Nome.upper()}')
print(f'Seu nome em minúsculas é {Nome.lower()}')
print(f'Seu nome tem ao todo {len(Nome)- Nome.count(" ")}')
separa = Nome.split()
print(f'Seu primeiro é {separa[0]} nome tem {len(separa[0])} letras')

