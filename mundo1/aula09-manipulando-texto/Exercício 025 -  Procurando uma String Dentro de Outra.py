#Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.
nome = input('Qual é o seu nome completo? ').strip().title()
print(f'Seu nome tem Silva? {"Silva" in nome.split()}')
