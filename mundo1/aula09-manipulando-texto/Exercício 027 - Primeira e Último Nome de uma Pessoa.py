#Crie um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separademente.
nome = input('Qual é o seu nome completo? ').strip().split()
print(f'O seu primeiro nome é {nome[0]} e o último é {nome[len(nome)-1]}.')
