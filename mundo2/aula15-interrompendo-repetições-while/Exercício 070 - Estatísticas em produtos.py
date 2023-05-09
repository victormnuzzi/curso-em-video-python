# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar.
# No final mostre:
# A) Qual é o total gasto na compra.
# B) Quantos produtos custam mais de R$1000,00.
# C) Qual é o nome do produto mais barato.

tot = prod = bar = cont = 0
print('-' * 45)
print('             LOJA SUPER BARATÃO')
print('-' * 45)
prodbar = ' '
while True:
    nome = input('Nome do produto: ')
    pre = float(input('Preço: R$'))
    tot += pre
    cont += 1
    if pre > 1000:
        prod += 1
    if bar > pre or cont == 1:
        prodbar = nome
        bar = pre
    resp = ' '
    while resp not in 'SN':
        resp = input('Deseja continuar? [S/N] ').strip().upper()[0]

    if resp == 'N':
        break
print('{:-^40}'.format(' FIM DO PROGRAMA '))
print(f'O total da compra foi R${tot:.2f}.\nTemos {prod} produtos custando mais de R$1000,00.')
print(f'O produto mais barato foi {prodbar} que custa R${bar:.2f}.')
