#Crie um programa que leia um número Real qualquer pelo telcado e mostre na tela a sua porção inteira.
from math import trunc
num = float(input('Digite um número Real: '))
print(f'O número {num} tem a parte inteira {trunc(num)}')
