# Crie um programa que leia um número inteiro e diga se ele é ou não um número primo.

div = 0
num = int(input('Digite um número: '))
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[32m', end=' ')
    else:
        print('\033[31m', end=' ')
    print(f'{c}', end=' ')
    if num % c == 0:
        div += 1
print(f'\n\033[mO número \033[35m{num}\033[m nome foi dividido \033[m{div}\033[m vezes.')

if div == 2:
    print('Por isso ele \033[32mé\033[m \033[34mprimo\033[m.')
else:
    print('Por isso ele \033[31mnão\033[m é \033[34mprimo\033[m.')

