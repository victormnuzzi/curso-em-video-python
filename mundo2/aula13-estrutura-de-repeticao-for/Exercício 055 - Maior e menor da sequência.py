# Crie um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input(f'Qual é o seu peso da {p} pessoa? (kg) '))
    if p == 1:
        maior = peso
        menor = peso
    if peso >= maior:
        maior = peso
    if peso <= menor:
        menor = peso
print(f'O maior peso foi de {maior:.1f} kg.\nO menor peso foi de {menor:.1f} kg.')
