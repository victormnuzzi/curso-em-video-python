# Crie um programa que leia o nome, idade e sexo de 4 pessoas. No final, mostre:
# - A média de idade do grupo
# - Qual é o nome do homem mais velho
# - Quantas mulheres tem menos de 20 anos
média = 0
homem = 0
mulher = 0
idade_mais_velho = 0
nome_homem = '.'
for c in range(1, 5):
    i = int(input(f'Idade da {c}ª pessoa: '))
    n = input(f'Nome da {c}ª pessoa: ').strip().capitalize()
    s = input(f'Sexo da {c} pessoa (M/F): ').strip().upper()
    print('-=' * 15)

    if c == 1:
        média = i
    else:
        média += i
    if s == 'M':
        homem += 1
    elif s == 'F' and i < 20:
        mulher += 1

    if c == 1 and s == 'M':
        idade_mais_velho = i
        nome_homem = n
    if s == 'M' and idade_mais_velho < i:
        idade_mais_velho = i
        nome_homem = n

médiac = média / 4

if mulher == 0:
    mulher = 'Nenhuma'

print(f'A média de idade do grupo é {médiac:.1f}.')

if idade_mais_velho == 0:
    print('Não há nenhum homem no grupo.')
else:
    print(f'O homem tem {idade_mais_velho} anos e se chama {nome_homem}.')

if mulher > 1:
    print(f'Ao todo, {mulher} mulheres tem menos de 20 anos.')
else:
    print(f'Ao todo, {mulher} mulher tem menos de 20 anos.')
