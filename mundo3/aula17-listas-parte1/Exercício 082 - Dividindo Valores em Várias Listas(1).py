''' Crie um programa que vai ler ários números e colcoar em uma lista
Depois disso, crie duas listas extras que vao contar apenas 
os valores pares e os valores ímpares digitados, respectivamente.
No final, mostre o conteúdo das três listas geradas.'''

# listas
lista = []
par = []
impar = []

# while com flag de quer continuar
while True:
    lista.append(int(input('Digite um número: ')))
    if n % 2 == 0: 
        par.append(n)
    else:
        impar.append(n)
    r = input('Quer continuar? [S/N] ').split()[0]
    if r in 'Nn':
        print('-=' * 40)
        print(f'A lista completa é {lista}.')
        print(f'A lista dos pares é {par}.')
        print(f'A lista dos ímpares é {impar}.')
        break


