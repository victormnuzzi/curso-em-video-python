# Crie um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# - 1 para binário
# - 2 para octal
# - 3 para hexadecimal
n = int(input('Qual número inteiro você deseja converter? '))
print('Base de conversão:')
print('[ 1 ] BINÁRIO')
print('[ 2 ] OCTAL')
print('[ 3 ] HEXADECIMAL')
o = int(input('Escolha uma das opções: '))
if o == 1:
    print(f'O número {n} convertido em BINÁRIO é igual a {bin(n)[2:]}.')
elif o == 2:
    print(f'O número {n} convertido em OCTAL é igual a {oct(n)[2:]}.')
elif o == 3:
    print(f'O número {n} convertido em HEXADECIMAL é igual a {hex(n)[2:]}.')
else:
    print('Erro. Escolha uma opção válida.')
