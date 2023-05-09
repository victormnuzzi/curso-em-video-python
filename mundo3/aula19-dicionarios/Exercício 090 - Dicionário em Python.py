'''
Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário
No final, mostre o conteúdo da estrutura na tela.
'''
aluno = {}
# aluno = {'nome': input('Nome: '), 'média': float(input(f'Média de {aluno['nome']}: '))}
aluno['Nome'] = input('Nome: ')
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Média'] >= 6:
    aluno['Situação'] = 'aprovado'
else: 
    aluno['Situação'] = 'reprovado'
for k, v in aluno.items():
    print(f'  - {k} é igual a {v}.')


# print('Situação é igual a ')
