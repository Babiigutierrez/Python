while True:
    Núm = int(input('Quer ver a tabuada de qual valor?'))
    if Núm < 0:
        break
    print('-'*34)
    print(f'''{Núm} x 1 = {Núm*1}
{Núm} x 2 = {Núm*2}
{Núm} x 3 = {Núm*3}
{Núm} x 4 = {Núm*4}
{Núm} x 5 = {Núm*5}
{Núm} x 6 = {Núm*6}
{Núm} x 7 = {Núm*7}
{Núm} x 8 = {Núm*8}
{Núm} x 9 = {Núm*9}
{Núm} x 10 = {Núm*10} ''')
    print('-' *34)
print('PROGRAMA TABUADA ENCERRADO. Volte sempre!')
