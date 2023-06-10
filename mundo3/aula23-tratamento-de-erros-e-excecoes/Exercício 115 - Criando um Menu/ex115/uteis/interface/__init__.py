from time import sleep

def tamPrograma():
    '''
    -> Definir tamanho do formato do programa
    :return: O tamanho do formato do programa
    '''
    tam_programa = 50
    return tam_programa

def linha(c='-',t=0):
    '''
    -> Printar uma linha de caracteres c com um tamanho t
    :param c: O caractere escolhido, pré-definido como -
    :param t: O tamanho da linha, pré-definido como 0
    '''
    print(c*t)


def titulo(text='',c='',t=tamPrograma()):
    '''
    -> Printar um título centralizado entre X caracteres
    :param text: O texto do título, pré-definido como ''
    :param c: O caractere escolhido, pré-definido como -
    :param t: O tamanho do título, pré-definido como ''
    '''
    print()
    linha(c, t)
    print(text.center(len(c*t)))
    linha(c, t)
    print()
    sleep(0.5)


def menuOpcoes(list=[], text=''):
    '''
    -> Printar um menu com x opções
    :param list: A lista com as opções
    :param text: O título do menu
    :return: A quantidade de opções
    '''
    if text != '':
        print()
        print(text.center(tamPrograma()))
    linha('-', tamPrograma())
    cont = 0 # contador de opções
    for opcao in list:
        cont += 1
        print(f'\033[33m[{cont}]\033\033[34m {opcao}\033[m')
    linha('-', tamPrograma())
    print()
    return cont


        