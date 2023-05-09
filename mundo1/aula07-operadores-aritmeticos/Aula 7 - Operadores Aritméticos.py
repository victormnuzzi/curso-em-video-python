# Operadores Aritméticos

nome = str(input('Qual o seu nome? '))
print(f'Prazer em te conhecer {nome}!')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro: '))
s = n1+n2
m = n1*n2
d = n1/n2
p = n1**n2
print(f'A soma é {s}, o produto é {m}, a divisão é {d:.3f} e a potência é {p}.', end='')
print('Deseja saber mais alguma coisa?')
