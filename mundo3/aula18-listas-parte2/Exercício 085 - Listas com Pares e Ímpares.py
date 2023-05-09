'''
Crie um programa onde o usuário possa digitar sete valores numéricos 
e cadastre-os em uma lista única que mantenha separado os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.'''

# criar lista
numeros = [[], []]

# for pois loop tem limite definido:
for i in range(0,7):
    n = int(input(f'Digite o {i + 1}o valor: '))
    if n % 2 == 0:
        numeros[0].append(n)
    if n % 2 != 0:
        numeros[1].append(n)
numeros[0].sort()
numeros[1].sort()
print('-=' * 20)
print(f'Os valores pares digitados foram {numeros[0]}.')
print(f'Os valores ímpares digitados foram {numeros[1]}.')