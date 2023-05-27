def fatorial(n):
    '''
    -> Calcular o fatorial de um valor
    :param n: O valor que será calculado do fatorial
    :param f: O resultado do fatorial
    :return: O fatorial do valor
    '''
    f = 1
    for c in range (1, n+1):
        f *= c
    return f

def dobro(n):
    '''
    -> Calcular o dobro de um valor
    :param n: O valor que será dobrado
    :return: O valor dobrado
    '''
    return 2 * n

def triplo(n):
    '''
    -> Calcular o triplo de um valor
    :param n: O valor que será triplicado
    :return: O valor triplicado
    '''
    return 3 * n

