'''
Crie um programa onde 4 jogadores joguem um dado e teham resultados aleatórios.
Gurade esses resulatdos em um dicionário. 
No final, coloque esse dicionário em ordem, savendo que o vencedor tirou o aior número no dado.
'''

from random import randint  # sortear numeros
from time import sleep  # delay entre as jogadas
from operator import itemgetter  # 

dados = {'jogador1': randint(1,6),
'jogador2': randint(1,6),
'jogador3': randint(1,6),
'jogador4': randint(1,6)
}

print('\nValores sorteados:')

for k, v in dados.items():
    sleep(1)
    print(f'     O {k} tirou {v}.')  # jogador tal tirou x
sleep(1)

ranking = {}

print('\nRanking dos jogadores:')

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)  # irá criar uma lista ordenando o dicionário com base no value do dicionario dados

for cont, v in enumerate(ranking):
    sleep(1)
    print(f'     {cont}º lugar: {v[0]} com {v[1]}.')
