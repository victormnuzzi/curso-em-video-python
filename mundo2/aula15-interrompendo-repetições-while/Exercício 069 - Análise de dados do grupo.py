# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
# No final, mostre:
# A) Quantas pessoas tem mais de 18 anos.
# B) Quantos homens fora m cadastrados
# C) Quantas mulheres tem menos de 20 anos.

h = m = maior = 0
while True:
    print('-' * 30)
    print('     CADASTRE UMA PESSOA')
    print('-' * 30)
    i = int(input('Idade: '))
    if i >= 18:
        maior += 1
    s = ' '
    while s not in 'MF':
        s = input('Sexo: [M/F] ').upper().strip()[0]
    if s == 'M':
        h += 1
    elif s == 'F' and i < 20:
        m += 1
    print('-' * 30)
    con = ' '
    while con not in 'SN':
        con = input('Deseja continuar? [S/N] ').upper().strip()[0]
    if con == 'N':
        break
print(f'\nTotal de pessoas maiores de 18 anos: {maior}\nAo todo temos {h} homens cadastrados.\nE temos {m} mulheres com menos de 20 anos.')
