# Crie um programa que leia dois valores e mostre um menu como o ao lado na tela:
# Seu programa deverá realizar a opeação solicitada em cada caso.
# [1] somar
# [2] multiplicar
# [3] maior
# [4] novos números
# [5] sair do programa

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
o = 0
while o != 5:
    print('-=' * 15)
    print('[1] Somar \n[2] Multiplicar \n[3] Qual é o maior \n[4] Novos números \n[5] Sair do programa')
    print('-=' * 15)
    o = int(input('>>>> Qual a sua opção? '))
    print('')
    if o == 1:
        print(f'A soma \033[34m{v1}\033[m + \033[32m{v2}\033[m é \033[35m{v1+v2}\033[m.')
    elif o == 2:
        print(f'O resultado de \033[34m{v1}\033[m x \033[32m{v2}\033[m é \033[35m{v1*v2}\033[m.')
    elif o == 3:
        if v1 > v2:
            print(f'Entre \033[34m{v1}\033[m e \033[32m{v2}\033[m, o maior valor é \033[34m{v1}\033[m é maior.')
        else:
            print(f'Entre \033[34m{v1}\033[m e \033[32m{v2}\033[m, o maior valor é \033[34m{v2}\033[m.')
    elif o == 4:
        v1 = int(input('Primeiro valor: '))
        v2 = int(input('Segundo valor: '))
if o == 5:
    print('')
    print('O programa foi finalizado.')
