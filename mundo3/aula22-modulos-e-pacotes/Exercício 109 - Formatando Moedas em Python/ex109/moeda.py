def aumentar(preco=0, taxa=0, formato=False):
    '''
    -> Calcular um aumento sobre um preço
    :param preco: O preço que sofrerá a taxa, sendo pré-definido como 0
    :param taxa: A taxa que será aplicada ao preço, sendo pré-definida como 0
    :param formato: Define se o valor final será formatado com o formato da moeda R$, sendo pré-definido como False
    :param res: O resultado do preço após a taxa
    :return: O valor formatado após o aumento
    '''
    res = preco * (1 + taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    '''
    -> Calcular uma diminuição sobre um preço
    :param preco: O preço que sofrerá a taxa, sendo pré-definido como 0
    :param taxa: A taxa que será aplicada ao preço, sendo pré-definida como 0
    :param formato: Define se o valor final será formatado com o formato da moeda R$, sendo pré-definido como False  
    :param res: O resultado do preço após a taxa
    :return: O valor após a diminuição
    ''' 
    res = preco * (1 - taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0,formato=False):
    '''
    -> Calcular o dobro de um valor
    :param preco: O valor que será dobrado, sendo pré-definido como 0
    :param formato: Define se o valor final será formatado com o formato da moeda R$, sendo pré-definido como False
    :param res: O resultado do dobro do valor
    :return: O dobro do valor
    '''
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    '''
    -> Calcular a metade de um valor
    :param preco: O valor que será dividido, sendo pré-definido como 0
    :param formato: Define se o valor final será formatado com o formato da moeda R$, sendo pré-definido como False
    :param res: O resultado da metade do valor
    :return: A metade do valor
    '''
    res = preco / 2
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    '''
    -> Formatar o valor no formato R$
    :param preco: O valor que será formatado, sendo pré-definido como 0
    :param moeda: A moeda que o valor será formatado, sendo pré-definido como "R$"
    :return: O valor formatado
    '''
    return f'{moeda}{preco:.2f}'.replace('.',',')


