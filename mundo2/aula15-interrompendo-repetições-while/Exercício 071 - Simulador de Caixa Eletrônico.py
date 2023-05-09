# Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.

print('=' * 30)
print('{:^30}'.format('BANCO'))
print('=' * 30)
v = int(input('Que valor você deseja sacar? R$'))
totcéd = 0
céd = 50
while True:
    if v >= céd:
        v -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de {céd}.')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if v == 0:
            break
