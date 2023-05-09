'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

sorteio = []
print('=' * 30, '\n{:^30}'.format('JOGA NA MEGA SENA'))
print('=' * 30)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))

print('\n{:-^40}'.format('  SORTEANDO {} JOGOS  ').format(jogos), '\n')
sleep(1)
for j in range(0, jogos):
    for s in range(0, 6):
        n = randint(1, 60)
        while True:
            if n not in sorteio:
                sorteio.append(n)
                break
            else:
                n = randint(1, 60)
    sorteio.sort()
    print(f'Jogo {j + 1}:  ', sorteio)
    sleep(1)
    sorteio.clear()
print('\n{:=^40}'.format(' < BOA SORTE > '))
