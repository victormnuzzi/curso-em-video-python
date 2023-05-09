#Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".
c = input('Digite o nome da cidade: ').strip().upper()
print('SANTO' in c[:5])
