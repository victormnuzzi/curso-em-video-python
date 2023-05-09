#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
num = str(input('Digite o número: ')).strip()

if len(num) > 4:
    print('Erro. Digite um número com no máximo 4 digitos.')
if len(num) == 4:
     print(f'Unidade: {num[0]}')
     print(f'Dezena: {num[1]}')
     print(f'Centena: {num[2]}')
     print(f'Milhar: {num[3]}')
if len(num) == 3:
     print(f'Unidade: {num[0]}')
     print(f'Dezena: {num[1]}')
     print(f'Centena: {num[2]}')
if len(num) == 2:
    print(f'Unidade: {num[0]}')
    print(f'Dezena: {num[1]}')
if len(num) == 1:
    print(f'Unidade: {num[0]}')