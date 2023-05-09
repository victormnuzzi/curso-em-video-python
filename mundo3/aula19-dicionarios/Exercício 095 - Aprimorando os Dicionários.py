'''
Aprimore o DESAFIO 93 para que ele funcione com vários jogadores, 
incluindo um sitema de visualização de detalhes do aproveitamento de cada jogador.
'''

resp = ''
jogadores = []  # lista com os dicionarios (de cada jogador)
jogador = {}  # dicionario
gols = []  # lista vai ser usada no for
while True:
    jogador['Nome'] = input('Nome do Jogador: ')  # nome do jogador  no dicionario
    jogador['Partidas'] = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))  # partidas do jogador no dicionario
    for p in range(0, jogador['Partidas']):  # ver quantos gols a cada partida
        gols.append(int(input(f'   Quantos gols na partida {p + 1}? ')))
    jogador['Gols'] = gols[:]  # dicionario Gols ganha cópia do valor da lista gols
    jogador['Total'] = sum(gols)
    jogadores.append(jogador)
    jogador = {}
    gols = []
    resp = input('Quer continuar? [S/N] ').upper()[0]  # quer adicionar mais um jogador?
    if 'N' in resp:
        break
    elif resp != 'S':  # se a resposta do continuar nao for Sim/variacoes:
        while resp != 'N' and resp != 'S':
            resp = input('\033[32mErro!\033[m Por favor digite novamente. \nQuer continuar? [S/N] ').upper()[0]
        if resp == 'N':
            break

print('-=-=' * 20)  # estética
print(f'{"Núm":<4}', f'{"Nome":<13}', f'{"Gols":<16}', f'{"Total":<5}')  # print dos t'itulos da tabela com espacamento
print('-' * 45)  # estética

for k, v in enumerate(jogadores):
    print(f'{k:^3}', end='')
    for d in v.values():
        print(f'{str(d):<12}', end='')
    print()

while True:  #laço para dados de cada jogador
    print('-' * 45)  # estética
    dados = int(input('Mostrar dados de qual jogador? (999 para parar) '))  
    if dados <= 0 or dados > cont2 and dados != 999:  # se o num for menor ou maior que os num dos jogadores
        print(f'\033[31mErro!\033[mNão existe jogador com Núm {dados}!')  # ERRO
    else:  # se num estiver certo:
        print(f'{"--":^4}', f'Levantamento do jogador {jogadores[dados - 1]["Nome"]}:')  # printar o titulo dos dados do jogador escolhido
        cont2 = 0  # definir contador n sei pra q
        for cont2 in range(0, jogadores[dados - 1]["Partidas"]):  # para contador2 no raio de 0 ate o numero de partidas do jogador escolhido(dados - 1 por causa da posicao)
            print(f'    No jogo {cont2 + 1} fez {jogadores[dados - 1]["Gols"][cont2]} gols.')  # no jogo cont2 + 1, o jogador fez x (lista de jogadores[jogador escolhido da tabela, dicionario Gols(para pegar a lista dos gols), cont2 por causa do numero do jogo y])
            if jogadores[dados - 1]["Partidas"] == cont2:  # se o numero de partidas do jogador escolhido na tabela for igual ao contador, significa que nao havera mais um indice da lista para puxar o num do jogo e quantos gols nessa partida
                break 
    if dados == 999:  # condicao de parada
        print('\n\033[32mVolte sempre!\033[m')
        break
