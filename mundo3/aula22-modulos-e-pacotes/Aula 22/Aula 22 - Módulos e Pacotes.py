# Módulos (Parte 1)
'''
import uteis

num = int(input('Digite um valor: '))
fat = uteis.fatorial(num)
print(f'\nO fatorial de {num} é {fat}.')
print(f'\nO dobro de {num} é {uteis.dobro(num)}.')
print(f'\nO triplo de {num} é {uteis.triplo(num)}.\n')
'''

# Pacotes (Parte 2)

from uteis import numeros

num = int(input('Digite um valor: '))
fat = numeros.fatorial(num)
print(f'\nO fatorial de {num} é {fat}.')
print(f'\nO dobro de {num} é {numeros.dobro(num)}.')
print(f'\nO triplo de {num} é {numeros.triplo(num)}.\n')