"""
FUPQ tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

def voto(ano_nasc):
    idade = 2023 - ano_nasc
    if 60 > idade >= 18:
        frase = f'Com {ano_nasc} anos: VOTO OBRIGATÓRIO.'
    elif 18 > idade >= 16:
        frase = f'Com {ano_nasc} anos: VOTO OPCIONAL..'
    else:
        frase = f'Com {ano_nasc} anos: NÃO VOTA.'
    return frase 


# Programa principal
print('-' * 30)
ano = int(input('Em que ano você nasceu? '))
voto(ano)

