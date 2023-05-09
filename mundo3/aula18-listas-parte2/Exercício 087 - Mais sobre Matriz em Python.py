'''
Aprimore o desafio anterior, mostrando no final:

A) A soma de todos os valores pares digitados.

B) A soma dos valores da terceira coluna.

C) O maior valor da segunda linha.
'''
'''valores = []
cont1 = cont2 = cont3 = a = b = c = 0
for i in range(0, 9):
    valores.append(int(input(f'Digite um valor para [{cont1}, {cont2}] ')))
    cont2 += 1
    if cont2 == 3:
        cont2 = 0
        cont1 += 1
print('-=' * 25)
for i in valores:
    cont3 += 1
    if cont3 == 2:
        if i > c:
            c = i
    if cont3 == 3:
        print('[{: ^5}]'.format(i))
        cont3 = 0
        b += i
    else:
        print('[{: ^5}]'.format(i), end='')
    if i % 2 == 0:
        a += i
    

print('-=' * 25, f'\nA soma dos valores pares é {a}.')
print(f'A soma dos valores da terceira coluna é {b}')
print(f'O maior valor da segunda linha é {c}.')'''

a = b = mv = 0
matriz = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}] ')))

print('-=' * 25)

for l in range(0,3):
    for c in range(0,3):
        print(f'[{matriz[l][c]: ^5}]', end='')
        if c == 2:
            b += matriz[l][c]
        if matriz[l][c] % 2 == 0:
            a += matriz[l][c]
        if c == 1:
            mv = matriz[l][c]
    print()

print('-=' * 25, f'\nA soma dos valores pares é {a}.')
print(f'A soma dos valores da terceira coluna é {b}.')
print(f'O maior valor da segunda linha é {mv}.')
