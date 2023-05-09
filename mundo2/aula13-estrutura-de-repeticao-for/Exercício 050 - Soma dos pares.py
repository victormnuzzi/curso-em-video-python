# Crie um programa que leia seis número inteiros e mostre a soma apenas daqueles que forem pares. Se o valor for ímpar, desconsidere-o.

s = 0
cont = 0
for c in range (0, 6):
    n = int(input('Digite um valor inteiro: '))
    if n % 2 == 0:
        s += n
        cont += 1
print(f'Você informou {cont} pares e soma dos números é {s}.')