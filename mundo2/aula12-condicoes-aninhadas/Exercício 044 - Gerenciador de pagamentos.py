# Crie um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - a vista dinheiro/cheque: 10% de desconto
# - em até 2x no cartão: preço normal
#  -3x ou mais no cartão: 20% de juros

print('{:=^40}'.format('Lojas Tchuscolandia'))
v = float(input('Preco das compras: R$'))
print('FORMA DE PAGAMENTO')
print('[ 1 ] a vista dinheiro/cheque')
print('[ 2 ] a vista no cartao')
print('[ 3 ] 2x no cartao')
print('[ 4 ] 3x ou mais no cartao')
fp = int(input('Qual das opcoes acima? '))
if fp == 1:
   print(f'Voce deve pagar R${v * 0.9:.2f}.')
elif fp == 2:
   print(f'Voce deve pagar R${v:.2f}.')
elif fp == 3:
   print(f'Voce deve pagar R${v:.2f}.')
elif fp == 4:
   print(f'Voce deve pagar R${v * 1.2:.2f}.')
else:
   print('\033[1;31mERRO\033[m. Voce deve selecionar uma das 4 opcoes.')
