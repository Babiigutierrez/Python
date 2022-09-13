from time import sleep
Núm1 = float(input('Digite o Primeiro Número:'))
Núm2 = float(input('Digite o Segundo Número:'))
Desejo = 0
while Desejo !=5:
    Desejo = int(input('''Menu da Matemática 
[1] Somar
[2] Multiplicar
[3] Maior
[4] Novos Números
[5] Sair do Programa.
O que você deseja?'''))
    if Desejo ==1:
        print(f'{Núm1} + {Núm2} = {Núm1 + Núm2}')
    elif Desejo == 2:
       print(f'{Núm1} * {Núm2} = {Núm1*Núm2}')
    elif Desejo ==3:
        if Núm1 > Núm2:
            print(f'O {Núm1} é maior que {Núm2}')
        elif Núm2 > Núm1:
            print(f'O {Núm2} é maior que {Núm1}')
        else:
            print(f'Os números {Núm1} e {Núm2} são iguais.')
    elif Desejo ==4:
        print(f'Você selecionou a opção {Desejo}:Novos Valores')
        Núm1 = float(input('Digite um novo valor:'))
        Núm2 = float(input('Digite um novo valor:'))
    elif Desejo == 5:
        print('Finalizando o programa...')
        sleep(2)
        print('Muito Obrigada e Volte Sempre!')
    else:
        print('Opção Inválida.Por favor, tente novamente')