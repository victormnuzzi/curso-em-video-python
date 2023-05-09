# Crie um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

vc = float(input('Qual é o valor da casa que voce deseja comprar? R$'))
s = int(input('Qual é o seu salario? R$'))
t = int(input('Em quantos anos voce pagara pela casa? '))
prest = vc/(t*12)
if prest > s * 1.3:
   print(f'O emprestimo bancario foi \033[1;31mnegado\033[m, pois a prestacao mensal de R${prest:.2f} \033[1;31mexcede\033[m 30% ou mais do seu salario.')
else:
   print(f'O emprestimo bancario foi \033[1;32maceito\033[m!!! Voce devera pagar mensalmente um valor de \033[1;32mR${prest:.2f}\033[m por \033[33m{t} anos\033[m para pagar o valor \033[32mR${vc:.2f}\033[m referente à casa.')