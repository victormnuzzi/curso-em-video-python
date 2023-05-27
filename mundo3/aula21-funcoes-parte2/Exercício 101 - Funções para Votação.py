"""
FUPQ tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""


def voto(an):
    '''
    -> Verifica a situação do voto do usuário
    :param an: O ano de nascimento do usuário
    :return: A situação do voto do usuário
    '''
    from datetime import date
    aa = date.today().year
    i = aa - an
    if 60 > i >= 18:
        return f'Com {i} anos: VOTO OBRIGATÓRIO.'
    elif 18 > i >= 16 or i > 65:
        return f'Com {i} anos: VOTO OPCIONAL..'
    else:
        return f'Com {i} anos: VOTO NEGADO.'


# Programa principal
print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
print(voto(ano)) # voto(ano) armazena o "valor" do return e precisa do print para mostrar esse "valor"

