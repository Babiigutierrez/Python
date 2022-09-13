Num = int(input('Digite um número inteiro:'))
print('''Escolha uma das bases para conversão:
 [1] Converter para BINÁRIO
 [2] Converter para OCTAL
 [3] Converter para HEXADECIMAL ''')
Opção = int(input('Sua opção:'))
if Opção == 1:
    print(f'{Num} convertido para BINÁRIO é igual à {bin(Num) [2:]}.')
elif Opção == 2:
    print(f'{Num} convertido para OCTAL é igual à {oct(Num) [2:]} .')
else:
    print(f'{Num} convertido para HEXADECIMAL é igual à {hex(Num) [2:]}.')