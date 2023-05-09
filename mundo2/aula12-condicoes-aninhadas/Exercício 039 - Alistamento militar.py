# Crie um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar
# - Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Ano de nascimento: '))
mes = int(input('Mes de nascimento (número): '))
ano_atual = date.today().year
idade = ano_atual - ano
alist = ((ano + 18) - ano_atual) * 12
if alist < 0:
    alist_ja = alist * (-1)
elif alist == 0:
    alist_esta = 12 - mes

if idade < 17:
    print(f'O jovem ainda vai se alistar no exército nos próximos {alist} meses.')
elif idade == 18:
    print(f'Está na hora do jovem se alistar no exército, ele tem até {alist_esta} meses.')
elif idade > 18:
    print(f'O jovem já deveria ter se alistado há {alist_ja} meses.')

