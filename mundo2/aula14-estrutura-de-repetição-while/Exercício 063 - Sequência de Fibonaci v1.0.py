# Crie um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Sequência de Fibonacci.
# Ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8

import math
# sequencia de fibonacci -> Fn = Fn-1 + Fn-2
# quantos termos voce quer saber? -> input
# mostrar X termos ate o Fim
cont = fib = 0
n1 = -1
n2 = 1
print('-' * 24, '\n Sequência de Fibonacci')
print('-' * 24)
num = int(input('Quantos termos você deseja saber? '))
while num != 0:
    cont += 1
    fib = n1 + n2
    n1 = n2
    n2 = fib
    print(fib, end=' -> ')
    if num == cont:
        num = 0
print('Fim'

