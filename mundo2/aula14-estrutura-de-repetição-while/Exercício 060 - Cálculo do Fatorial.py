# Crie um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
f = 1
n = int(input('Digite um número para calcular fatorial: '))
print(f'Calculando {n}! =', end=' ')
while n > 0:
        print(f'{n}', end='')
        print (' x' if n > 1 else ' =', end=' ')
        f *= n
        n -= 1
print(f'{f}')
