Número = ('zero', 'um' , 'dois' ,'três','quatro',
          'cinco','seis','sete','oito','nove','dez',
          'onze','doze','treze','quartoze','quinze',
          'dezesseis','dezessete','dezoito','dezenove','vinte' )
while True:
    Núm = int(input('Tente novamente. Digite um número entre 0 e 20:'))
    if 0 <= Núm <= 20:
        break
    print('Tente Novamente', end='')
print(f'Você digitou o número {Número[Núm]}')
