from time import sleep

def vInt(n=''):
    '''
    -> Verificar se input é int
    :param n: O texto que será verificado, pré-definido como ''
    :return: O número na forma de inteiro
    '''
    try:
        n = int(n)
    except ValueError: # ValueError ??
        print('\n\033[31mERRO! Por favor, digite um número inteiro válido.\033[m\n')
        sleep(1)
    else:
        return n
    

def vOpcao(tam_opcoes):
    '''
    -> Verificar se a opção é válida
    :param opcoes: A quantidade de opções do menu
    :return: A opção escolhida pelo usuário
    '''
    status = 1 # ligado
    while status == 1:
        escolha1 = input('\033[33mSua Opção: \033[m') # escolha
        escolha_int = vInt(escolha1) # verificar se é inteiro
        try:
            if escolha_int > tam_opcoes or 0 >= escolha_int: # se a escolha não estiver dentre as opções
                print('\n\033[31mERRO! Por favor, digite uma opção válida.\033[m\n') # print erro
            else:  # se estiver, termina o loop e retorna a escolha
                status = 0 # desligado
                return escolha_int
        except:
            continue
    sleep(1)

    
