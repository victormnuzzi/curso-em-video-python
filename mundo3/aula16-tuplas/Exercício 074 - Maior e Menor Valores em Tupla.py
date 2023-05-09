'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de númereos gerados e 
também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

valores = (randint(1, 10), randint(1, 10), randint(1,10), randint(1,10), randint(1,10))

print('Os números sorteados foram:', end=' ')
for num in valores:
    print(num, end=' ')
print(f'\nO menor valor sorteado foi {min(valores)} e o maior foi {max(valores)}.')