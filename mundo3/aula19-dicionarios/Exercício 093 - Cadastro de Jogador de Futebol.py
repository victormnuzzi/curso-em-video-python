'''
Cire um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o toal de gols feitos durante o campeonato.
'''

jogador = {}  # dicionario
gols = []  # lista vai ser usada no for
jogador['Nome'] = input('Nome do Jogador: ')  # nome do jogador  no dicionario
jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))  # partidas do jogador no dicionario
for p in range(0, jogador['Partidas']):  # ver quantos gols a cada partida
    gols.append(int(input(f'   Quantos gols na partida {p + 1}? ')))
jogador['Gols'] = gols[:]  # dicionario Gols ganha cópia do valor da lista gols

print('-=-=' * 20)
print(jogador)
print('-=-=' * 20)

for k in jogador:
    print(f'O campo {k} tem valor de {jogador[k]}.')
print('-=' * 20)

print(f'O jogador {jogador["Nome"]} jogou {jogador["Partidas"]}.')
for p in range(0, len(jogador['Gols'])):
    print(f'   => Na partida {p + 1}, fez {jogador["Gols"][p]} gols.')

print(f'Foi um total de {sum(gols)} gols.')
