# Crie um programa que leia vários n;umeros inteiros pelo teclado.
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.


#maior e menor -> loop -> while
# digite um numero -> input (armazenar numero)
# quer continuar? -> s ou n
# final -> quando 'N' -> maior numero e menor numero
n = maior = quant = menor = 0
perg = ''
while 'N' not in perg:
    n = int(input('Digite um número: '))
    perg = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    quant += 1
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
print(f'\nO maior valor é \033[35m{maior}\033[m e o menor valor é \033[34m{menor}\033[m.')

