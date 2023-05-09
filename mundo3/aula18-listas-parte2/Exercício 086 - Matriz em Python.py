'''
Crie um programa que crie uma matriz da dimensão 3x3
e preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
'''
'''
valores = []
cont1 = cont2 = cont3 = 0
for i in range(0, 9):
    valores.append(int(input(f'Digite um valor para [{cont1}, {cont2}] ')))
    cont2 += 1
    if cont2 == 3:
        cont2 = 0
        cont1 += 1

print('-=' * 25)

for i in valores:
    cont3 += 1
    if cont3 == 3:
        print('[{: ^5}]'.format(i))
        cont3 = 0
    else:
        print('[{: ^5}]'.format(i), end='')
'''

matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[c].append(int(input(f'Digite um valor para [{l}, {c}]')))

print('-=' * 25)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]: ^5}]', end ='')
    print('\n')