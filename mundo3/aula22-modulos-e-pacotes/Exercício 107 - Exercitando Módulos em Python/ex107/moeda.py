def aumentar(preco, taxa):
    '''
    -> Calcular um aumento sobre um preço
    :param preco: O preço que sofrerá a taxa 
    :param taxa: A taxa que será aplicada ao preço
    :return: O valor após o aumento
    '''
    res = preco * (1 + taxa/100)
    return res


def diminuir(preco, taxa):
    '''
    -> Calcular uma diminuição sobre um preço
    :param preco: O preço que sofrerá a taxa 
    :param taxa: A taxa que será aplicada ao preço
    :return: O valor após a diminuição
    ''' 
    res = preco * (1 - taxa/100)
    return res


def dobro(preco):
    '''
    -> Calcular o dobro de um valor
    :param preco: O valor que será dobrado
    :return: O dobro do valor
    '''
    res = preco * 2
    return res


def metade(preco):
    '''
    -> Calcular a metade de um valor
    :param preco: O valor que será dividido
    :return: A metade do valor
    '''
    res = preco / 2
    return res

