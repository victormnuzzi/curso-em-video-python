"""
FUPQ tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""

def voto(ano_nasc):
    idade = 2023 - ano_nasc
    if idade >= 18:
        print('Você deve votar.')
    elif 18 > idade >= 16:
        print('Voce já pode votar.')
    else:
        print('Você ainda não pode votar') 

voto(int(input('Digite o seu ano de nascimento: ')))

# %%
