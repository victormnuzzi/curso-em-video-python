# Crie um programa que leia o sexo de uma pessoa, mas só aceite os valores "M" ou "F". Caso esteja errado, peça a digitação novamente até ter um valor correto
s = input('Informe seu sexo: [M/F] ').upper()
while s != 'M' and s != 'F': #ou while s not in 'MF':
    s = input('\033[31mDados inválidos!\033[m Por favor, informe seu sexo: [M/F] ').upper()
print(f'Sexo {s} registrado com \033[32msucesso\033[m.')
