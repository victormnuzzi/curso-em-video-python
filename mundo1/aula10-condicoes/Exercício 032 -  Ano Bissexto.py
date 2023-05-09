# Crie um programa que leia um ano qualquer e mostre se ele é BISSEXTO.
ano = int(input('Qual é o ano que você deseja saber sobre? '))
print(f'O ano de {ano} é bissexto.' if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 else f'O ano de {ano} não é bissexto.')

#if ano % 4 == 0:
#    if ano % 100 == 0:
#        if ano % 400 == 0:
#            print(f'O ano de {ano} é bissexto.')
#        else:
#            print(f'O ano de {ano} não é bissexto.')
#    else:
#        print(f'O ano de {ano} é bissexto.')
#else:
#3    print(f'O ano de {ano} não é bissexto.')


#Como fazer para o python analisar o ano atual que está nesse computador.
# from datetime import date
#Mudar -> 'Qual é o ano que você deseja saber sobre? ' --> adicionar 'Digite 0 para analisar o ano atual. '
# if ano ==):
# ano = date.today().year