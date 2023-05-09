# Crie um programa que leia três números e mostre qual é o MAIOR e o MENOR.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

# É melhor considerar uma variável menor ou maior para simplificar o código.
if n1 > n2 and n1 > n3:
    print(f'O maior número é {n1}')
elif n2 > n1 and n2 > n3:
    print(f'O maior número é {n2}')
elif n3 > n1 and n3 > n2:
    print(f'O maior número é {n3}')

if n1 < n2 and n1 < n3:
    print(f'O menor número é {n1}')
elif n2 < n1 and n2 < n3:
    print(f'O menor número é {n2}')
elif n3 < n1 and n3 < n2:
    print(f'O menor número é {n3}')

# menor = a
# if b < a and b < c:
#   menor = b
# if c < a and c < b:
#   menor = c
# maior = a
# if b > a and b > c:
#   maior = b
# if c > a and c > b:
# maior = c
# print(f'O menor é {menor}.'
# print (f'O maior é {maior}.')
