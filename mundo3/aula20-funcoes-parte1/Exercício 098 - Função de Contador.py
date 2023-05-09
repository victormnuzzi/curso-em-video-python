'''
FUPQ tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo e realize a contagem.

Seu programa tem que realizar três contagens através da função criada:
a) De 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) Uma contagem personalidada
'''


from time import sleep

def lin():
    print('=-=' *12)

def contador(inicio, fim, passo):
    lin()
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    cont = inicio    
    abs(passo)
    if inicio < fim:
        while cont <= fim:
            print(f'{cont} ', end="", flush=True)
            cont += passo
            sleep(0.2)     
    else:
        passo *= -1
        while cont >= fim:
            print(f'{cont} ', end="", flush=True)
            cont += passo
            sleep(0.2)
    print('FIM!')     


# Programa principal
contador(1, 10, 1)
contador(10, 0, 2)

lin()
print('Agora é sua vez de personalizar o contador!')

inicio, fim, passo = int(input('Início: ')), int(input('Fim: ')), int(input('Passo: '))
if passo == 0:
    while passo == 0:
        print('ERRO! Digite um Passo diferente de 0.')
        passo = int(input('Passo: '))
contador(inicio, fim, passo)
