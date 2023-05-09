'''
Crie um programa que leia nome, sexo e idade de várias pessoas,
 guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
 No final, mostre:
 A) Quantas pessoas foram cadastradas;

 B) A média de idade do grupo;

 C) Uma lista com todas as mulheres;

 D) Uma lista com todas as pessoas com idade acima da média.

 '''
total_idade = 0  # para calcular media
mulheres = []
cadastro = []  #lista dos dicionarios

while True: 
    pessoa = {}
    pessoa['Nome'] = input('Nome: ')
    sexo = input('Sexo: [M/F] ')[0]
    if sexo in 'Ff':
        mulheres.append(pessoa["Nome"])
    while sexo not in 'MmFf':
        print('\033[31mERRO\033[m! Responda apenas M ou F.')
        sexo = input('Sexo: [M/F] ')
    if sexo in 'MmFf':
        pessoa['Sexo'] = sexo
    pessoa['Idade'] = int(input('Idade: '))
    total_idade += pessoa['Idade']  # somar idade para fazer media
    cadastro.append(pessoa)  #cadastrar pessoa na lista
    continuar = input('Quer continuar? [S/N] ')[0]
    while continuar not in 'NnSs':  # confirmar se usuario escreveu s ou n
        print('\033[31mERRO\033[m! Responda apenas S ou N.')
        continuar = input('Quer continuar? [S/N] ')[0]
    if continuar in 'Nn':  # se resposta for igual a nao, apra codigo
        break


print('-=' * 24)

print(cadastro)

print(f'A) Ao todo temos {len(cadastro)} pessoas cadastradas.')
media = total_idade / len(cadastro)
print(f'B) A média de idade é de {media} anos.')

if len(mulheres) > 0:
    print(f"As mulheres cadastradas foram ", end='')
    for i in range(0, len(mulheres)):
        print(mulheres[i], end=', ')
else:
    print('Não houve nenhuma mulher cadastrada.')

print('\nD) Lista das pessoas que estão acima da média:')

for i in range(0, len(cadastro)):
    while True:
        if cadastro[i]['Idade'] >= media:
            print(cadastro[i])
        break

print('\033[34m<<< ENCERRADO >>>\033[m')
