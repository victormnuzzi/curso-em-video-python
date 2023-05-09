"""
FUPQ tenha uma lista chamada números e duas funções chamas sorteio() e somaPar().
A primeira função vai sortear os números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores PARES sorteados pela função anterior.

"""
"""
# Com uma função
from random import randint
from time import sleep

def sorteio():
    valores = []
    soma = 0
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(0,5)
        valores.append(num)
        if num % 2 == 0:
            soma += num
        print(num, end=' ', flush=True)
        sleep(0.5)
    print(f'\nSomando os valores pares de {valores}, temos {soma}.\n')

sorteio()
"""
# Com as duas funções
from random import randint
from time import sleep

valores = []

def sorteio():
    print(f'Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        num = randint(0,10)
        valores.append(num)
        print(num, end=' ', flush=True)
        sleep(0.5)
    print('')

def somaPar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor  
    print(f'Somando os valores pares de {valores}, temos {soma}.\n')

sorteio()
somaPar(valores)
