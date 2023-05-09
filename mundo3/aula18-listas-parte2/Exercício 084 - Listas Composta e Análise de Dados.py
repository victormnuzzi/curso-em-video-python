''' Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

A) Quantas pessoas foram cadastradas.  # len(lista)

B) Uma listagem com as pessoas mais pesadas.

C) Uma listagem com as pessoas mais leves.'''

# lista
lista = []
p_maior = 0

# while infinito com flag break
while True:
    nome = input('Nome: ')
    peso = float(input('Peso em Kg: '))
    lista.append([nome, peso])

    if peso > p_maior:
        p_maior = peso
        p_menor = peso


    if p_menor > peso:
        p_menor = peso


    resp = input('Quer continuar? [S/N] ').upper().split()[0]
    if resp == 'N':
        break

print(f'\nAo todo, você cadastrou {len(lista)} pessoas.')

print(f'\nO maior peso foi de {p_maior:.1f}Kg. Peso de', end=' ') 

for p in lista:
    if p[1] == p_maior:
        print(p[0], end=' ')
    
print(f'\nO menor peso foi de {p_menor}Kg. Peso de', end=' ')

for p in lista:    
    if p[1] == p_menor:
        print(p[0], end=' ')
