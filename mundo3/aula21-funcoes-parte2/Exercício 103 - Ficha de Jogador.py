"""
FUPQ tenha uma função chamada ficha(), que receba dois parâmetros opcionais:
- nome de um jogador
- quantos gols ele marcou
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""

# função ficha(nome='<desconhecido>', gol=0)
def ficha(n='<desconhecido>',g=0):
    ''''
    -> Registro de nome de jogador e quantos gols ele fez
    :param n: O nome do jogador
    :param g: O número de gols marcados pelo jogador
    '''
    # return com nome e gols
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


# Programa principal

# input do nome
nome = input('Nome do Jogador:  ')

# input do gol
gol = str(input('Número de Gol(s): '))

# verificação para ver se gol é númerico 
if gol.isnumeric(): # se for, gol vira inteiro
    gol = int(gol)
else: # senão, gol recebe 0
    gol = 0

# Verificação para ver se nome sem espaço é vazio
if nome.strip() == '':
    ficha(g=0)
else:
    ficha(nome, gol)

