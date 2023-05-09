# Crie um programa q leia o nome completo de uma pessoa e mostre:
# 1) O nome com todas as letras maiúsculas
# 2) O nome com todas minúsculas
# 3) Quantas letras tem sem contar espaços
# 4) Quantas letras tem o primeiro nome
nome = str(input('Qual é o seu nome completo? ').strip())
sep = nome.split()
t = len(nome) - nome.count(' ')
pn = sep[0]
print(f'O seu nome minúsculo é {nome.lower()}.')
print(f'O seu nome maiúsculo é {nome.upper()}')
print(f'O seu nome tem {t}.')
print(f'O seu primeiro nome é {pn} e tem {len(pn)} letras.')
