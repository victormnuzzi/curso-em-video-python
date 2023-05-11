"""
FUPQ tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que será mostrado ou não na tela o processo de cálculo do fatorial
"""

# função fatorial(numero, show)
def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número inteiro escolhido pelo usuário
    :param n: O número inteiro a ser calculado
    :param show: (Opcional) Mostra ou não a conta
    :return: O valor do fatorial do número escolhido pelo usuário
    '''
    # verificacao se s é True (print do cálculo) ou False (sem print do cálculo)
    if show == True: 
        # loop para printar processo de cálculo
        for i in range(n, 0, -1): # vai do número até 0 (na verdade 1) e -1 porque ele vai do maior para o menor
            if i == 1: # se o index (número do cáculo do fatorial) for igual a 1, printar com =
                print(i, end=' = ')
            else:
                print(i, end=' x ')

    # calculo do fatorial
    for i in range(1, n):
        n *= i

    # return do fatorial
    return n


# Programa principal
mostrar = False
print('=-=' * 20) # estética

# input do usuário do número que será calculado
num = int(input('Digite um número inteiro que você deseja saber o fatorial: '))

# input do usuário para verificar se quer ver o cálculo
resp = input('Você deseja ver o cálculo? [S/N] ').upper()

# verificando se quer ver o cálculo
if resp == 'S':
    mostrar = True

# chamada da função
print(fatorial(num, mostrar))