# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JÚNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER
from datetime import date
an = int(input('Ano de nascimento: '))
atual = date.today().year
i = atual - an
if i <= 9:
    categoria = 'MIRIM'
elif 9 < i <= 14:
    categoria = 'INFANTIL'
elif  14 < i <= 19:
    categoria = 'JÚNIOR'
elif 19 < i <= 20:
    categoria = 'SÊNIOR'
else:
    categoria = 'MASTER'
print(f'O aluno tem {i} anos.')
print(f'Categoria: {categoria}')