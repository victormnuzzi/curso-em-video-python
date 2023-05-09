# Crie um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1.250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais, o aumento é de 15%.
s = float(input('Qual é o salário do funcionário? R$'))
if s > 1250:
    ns = s * 1.1
else:
    ns = s * 1.15
ns = f'{ns:_.2f}'
ns = ns.replace('.',',').replace('_','.')
print(f'Quem ganhava {s}, passa a ganahr R${ns}.')
