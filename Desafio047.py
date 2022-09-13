print('-=' *7)
print('\33[1;30mNúmeros Pares\33[m')
print('-=' *7)
print('Os números pares entre 1 e 50 são:')
for c in range (1,50+1):
    if c % 2 ==0:
        print(c, end=' ' )
print('Fim!')