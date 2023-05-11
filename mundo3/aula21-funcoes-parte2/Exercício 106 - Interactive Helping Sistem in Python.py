"""
Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra "FIM", o programa se encerrará.

OBS: use cores
"""
from time import sleep

# Tupla com cores
cores = (
    '\033[0m',         # 0 - sem cores
    '\033[0;30;41m',   # 1 - vermelho
    '\033[0;30;42m',   # 2 - verde
    '\033[0;30;43m',   # 3 - amarelo
    '\033[0;30;44m',   # 4 - azul
    '\033[0;30;45m',   # 5 - roxo
    '\033[7;30m',       # 6 - branco
)

# Função para printar um título personalizado
def titulo(t, c=0):
    '''
    -> Printar um título personalizado
    :param t: O texto do título
    :param c: A cor do título
    '''
    tam = len(t) + 6
    print()
    print(cores[c], end='')
    print('~' * tam)
    print(f'{t:^{tam}}')
    print('~' * tam)
    print(cores[0])
    print()

# Função para o usuário visualizar o manual de uma função/biblioteca
def pyhelp():
    while True:
        titulo('SISTEMA DE AJUDA PyHELP', 2)
        resp = input('Função ou Biblioteca (Digite "fim" para parar) > ').lower()
        if resp == 'fim':
            titulo('ATÉ LOGO!', 43)
            break
        else:
            titulo(f"Acessando o manual do comando '{resp}'", 5)
            sleep(1)
            help(resp)


# Programa principal
pyhelp()
