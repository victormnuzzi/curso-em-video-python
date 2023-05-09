'''Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os em um dicionário se
por acaso o CTPS for diferente de ZERO, o dicionário também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''
#  aposentar --> 35 de contibuição

from datetime import date

ano_atual = date.today().year


n = input('Nome: ')
an = int(input('Ano de Nascimento: '))
cpts = int(input('Carteira de Trabalho (0 não tem): '))

if cpts != 0:
    ano_c = int(input('Ano de Contratação: '))
    s = int(input('Salário: R$ '))

    pessoa = {'Nome': n, 'Idade': ano_atual - an, 'CPTS': cpts, 'Ano de Contratação': ano_c, 'Salário': s, 'Aposentadoria': ano_c + 35 - 2003}
else:
    pessoa = {'Nome': n, 'Idade': ano_atual - an, 'CPTS': cpts}

print('-=' * 22)
for k, v in pessoa.items():
    print(f' -> {k} tem o valor de {v}.')



'''utilizar pessoa[variavel] = input(x)'''
