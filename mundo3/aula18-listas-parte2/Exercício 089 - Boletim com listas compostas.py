'''
Crie um programa que leia nome e duas notas de várias alunos
e guarde tudo em uma lista completa. 
No final, mostre um boletim contendo a média de cada um
e permita que o usuário possa mostrar as notas de cada aluno individualmente.
'''

alunos = []
aluno = []
while True:
    aluno.append(input('Nome: '))  
    aluno.append(float(input('Nota 1: ')))  
    aluno.append(float(input('Nota 2: ')))  
    alunos.append(aluno[:])
    aluno.clear()
    resp = input('Quer continuar? [S/N] ').split()[0]
    if resp in 'Nn':
        break
print('-=' * 22)
print('\nNº ', '{:<9}'.format('NOME'), 'MÉDIA')
print('-' * 20)
for a in range(0, len(alunos)):
    print(a + 1, '  {:<9}'.format(alunos[a][0]), '{:>6.1f}'.format((alunos[a][1] + alunos[a][2]) / 2))
print('-' * 20)
while True:
    num = int(input('\nMostrar notas de qual aluno? (999 interrompe) '))
    if num == 999:
        break
    if num > len(alunos) + 1:
        print('\033[31mERRO\033[m. Por favor, digite um aluno válido. ', end='')
    print(f'Notas de {alunos[num - 1][0]}:  {alunos[num - 1][1:]}\n')
print('FINALIZANDO...\n', 'Volte sempre!')