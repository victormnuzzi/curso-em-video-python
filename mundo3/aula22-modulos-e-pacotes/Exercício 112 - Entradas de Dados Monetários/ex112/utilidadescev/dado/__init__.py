def leiaDinheiro(msg=''):
    '''
    -> Verificar se o valor é um número válido no formato real
    :param msg: A frase do input do usuário, sendo pré-definida como ''
    :return: O preço em float
    '''
    valido = False
    while not valido:
        input_preco = input(msg).strip()
        if input_preco.isnumeric():
            valido = True
        elif input_preco.isalpha():
            print(f'\n\033[31mERRO! "{input_preco}" não é um preço válido.\033[m\n')
        elif input_preco.count('.') == 1:
            if input_preco.replace('.', '').isalpha():
                print(f'\n\033[31mERRO! "{input_preco}" não é um preço válido.\033[m\n')
            elif input_preco.replace('.', '').isalpha() is False:
                if input_preco.replace('.', '').isnumeric():
                    valido = True
                else:
                    print(f'\n\033[31mERRO! "{input_preco}" não é um preço válido.\033[m\n')
        elif input_preco.count(',') == 1: 
            if input_preco.replace(',', '').isalpha():
                print(f'\n\033[31mERRO! "{input_preco}" não é um preço válido.\033[m\n')
            else:
                if input_preco.replace(',', '').isnumeric():
                    input_preco = input_preco.replace(',', '.')
                    valido = True
                else:
                    print(f'\n\033[31mERRO! "{input_preco}" não é um preço válido.\033[m\n')
        else:
            print(f'\n\033[31mERRO! "{input_preco}" não é um preço válido.\033[m\n')

    return float(input_preco)
