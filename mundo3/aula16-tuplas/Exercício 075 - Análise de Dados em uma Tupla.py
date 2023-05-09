'''
Crie um programa que leia quatro valores pelo teclado e guarde-os em uma tupla.
No final mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
'''
valores = ()
pares = ()
for i in range(1,5):
    v = int(input(f'Digite o {i}º valor: '))
    valores += (v, )
    if v % 2 == 0:
        pares += (v, )


a = valores.count(9)
print(f'O número 9 apareceu {a} vezes.')
if 3 in valores:
    b = valores.index(3)
    print(f'O 1º valor 3 foi digitado na {b}ª posição.')
else:
    print('Não foi digitado o valor 3.')

print('Os números pares digitados foram: ', end='')
for p in pares:
    print(p, end=' ')
