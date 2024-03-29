"""
FUPQ tenha uma função leiaInt(), que vai funcionar de semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
Ex: n = leiaInt('Digite um n)
"""

def leiaInt(frase=''):
    '''
    -> Ler um texto e verificar se é um número inteiro
    :param frase: A frase do input na função
    :return: O número digitado pelo usuário na forma de inteiro
    '''
    while True:
        num = str(input(frase))
        if not num.isnumeric(): # se o num não for numérico, print do erro
            print('\033[31mERRO! Digite um número válido.\033[m') 
        else: 
            return int(num) # return funciona como um break


# Programa principal
n = leiaInt('Digite um número: ') # chamando a função
print(f'Você acabou de digitar o número {n}.') # print final