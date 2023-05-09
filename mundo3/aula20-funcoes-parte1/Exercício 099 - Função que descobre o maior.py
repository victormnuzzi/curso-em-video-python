"""
FUPQ tenha ua função chama maior(), que receba vários parâmetros com valores inteiros. 
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep

def maior(*valores):
    maior = cont = 0
    print('=-=' * 15)
    print('\nAnalisando os valores passados...')
    sleep(2)

    for num in valores:
        print(num, end=' ', flush=True)
        sleep(0.3)
        cont += 1
        if num > maior:
            maior = num

    sleep(0.5)
    print(f'Foram informados {cont} valores ao todo.')
    sleep(0.5)
    print(f'O maior valor foi {maior}.\n')
    sleep(2)



# Programa principal
maior(2, 9, 4, 5, 7, 1)

maior(4, 7, 0)

maior(1, 2)

maior()