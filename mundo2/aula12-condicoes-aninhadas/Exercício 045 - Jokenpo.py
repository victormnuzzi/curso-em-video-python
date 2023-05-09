# Crie um programa que faça o computador jogar Jokenpo com você
from random import randint
itens = ('PEDRA','PAPEL','TESOURA')
cjog = randint(0,2)

print('Suas opções:')
print('[ 1 ] PEDRA')
print('[ 2 ] PAPEL')
print('[ 3 ] TESOURA')
jog = int(input('Qual é a sua jogada? '))
print('JO \nKEN \nPO!!')
if jog == 1:
    jog = 'PEDRA'
elif jog == 2:
    jog = 'PAPEL'
elif jog == 3:
    jog = 'TESOURA'
else:
    print('\033[31mERRO\033[m.')
print('-=' * 10)
print(f'Computador jogou {itens[cjog]} \nJogador jogou {jog}')
print('-=' * 10)
if jog == 'PEDRA' and itens[cjog] == 'PAPEL' or jog == 'PAPEL' and itens[cjog] == 'TESOURA' or jog == 'TESOURA' and itens[cjog] == 'PEDRA':
    print(f'\033[35mCOMPUTADOR\033[m \033[32mVENCEU\033[M!!!')
elif itens[cjog] == 'PEDRA' and jog == 'PAPEL' or itens[cjog] == 'PAPEL' and jog == 'TESOURA' or itens[cjog] == 'TESOURA' and jog == 'PEDRA':
    print(f'\033[35mJOGADOR\033[m \033[32mVENCEU\033[M!!!')
elif jog == itens[cjog]:
    print('\033[1;34mEMPATE\033[m. Não houve vencedor.')
