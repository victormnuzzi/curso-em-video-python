def leiaInt(frase=''):
    '''
    -> Verificar se um input é int
    :param frase: A frase do input na função, pré-definida como ''
    :return: O número digitado pelo usuário
    '''
    while True:
        try:
            num = int(input(frase))
        except (ValueError, TypeError):
            print('\n\033[31mERRO! Digite um número válido.\033[m\n')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO! O usuário preferiu não informar nenhum número.\033[m\n')
            return 0
        else:
            return num


def leiaFloat(frase=''):
    '''
    -> Verificar se um input é float
    :param frase: A frase do input na função, pré-definida como ''
    :return: O número digitado pelo usuário 
    '''
    while True:
        try:
            num = float(input(frase))
        except (ValueError, TypeError):
            print('\n\033[31mERRO! Digite um número válido.\033[m\n')
            continue
        except KeyboardInterrupt:
            print('\n\033[31mERRO! O usuário preferiu não informar nenhum número.\033[m\n')
            return 0
        else:
            return num