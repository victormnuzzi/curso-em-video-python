# Crie um programa que leia vários números inteiros pelo teclado.
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).

nd = -1
s = -999
n = 0
while n != 999:
	n = int(input('Digite um número [999 para parar]: '))
	nd += 1
	s += n
print(f'Você digitou \033[32m{nd}\033[m números e a soma entre eles foi \033[34m{s}\033[m.')