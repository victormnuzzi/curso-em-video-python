# # Crie um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

cont = 0
sort = 1

print('-=' * 15)
print('\033[32mVAMOS JOGAR PAR OU ÍMPAR\033[m')
print('-=' * 15)

while True:
    sort = random.randint(0, 11)
    num = int(input('Digite um valor: '))
    par_ou_impar = input('Par ou Ímpar? [P/I] ').upper().strip()[0]
    print('-' * 40)
    print(f'Você jogou {num} e o computador jogou {sort}.')
    print('-' * 40)
    if (num + sort) % 2 == 0:
        if par_ou_impar == 'P':
            print('\033[32mVOCÊ GANHOU!\033[m Vamos jogar denovo.')
            cont += 1
        elif par_ou_impar == 'I':
            break
    else:
        if par_ou_impar == 'I':
            print('\033[32mVOCÊ GANHOU!\033[m Vamos jogar denovo.')
            cont += 1
        elif par_ou_impar == 'P':
            break
print(f'\033[31mVOCÊ PERDEU!!!\033[m Você venceu {cont} vezes.')
