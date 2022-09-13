from time import sleep
Festa = str(input('Qual é a comemoração?')).strip().title()
for c in range (10 , -1, -1):
    print(c)
    sleep(1)
print(f'Feliz {Festa} \U0001f386\U0001f386\U0001f386 ')
