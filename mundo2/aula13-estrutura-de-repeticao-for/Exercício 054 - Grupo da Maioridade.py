# Crie um programa que leia o ano de nascimento de sete pesoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

atual = date.today().year
nm = 0
m = 0
for c in range(1, 8):
    an = int(input(f'Ano de nascimento da {c}ª pessoa: '))
    i = atual - an
    if i >= 18:
        m += 1
    elif i < 18:
        nm += 1
print(f'Ao todo, {m} pessoas são maiores de idade e {nm} pessoas ainda não atingiram a maioridade.')
