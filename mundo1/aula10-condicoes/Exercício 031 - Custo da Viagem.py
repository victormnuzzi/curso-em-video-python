# Crie um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200km e R$0,45 para viagens mais longas.
p = int(input('Qual a distância da viagem em Km? '))
print(f'Sua viagem custará R${p * 0.5:.2f}.' if p <= 200 else f'Sua viagem custará R${p * 0.45:.2f}.')
