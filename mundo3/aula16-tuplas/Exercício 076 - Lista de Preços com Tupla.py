'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos
preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em uma forma tabular.
'''

print('-' * 40)
print('{:^40}'. format('LISTAGEM DE PREÇOS'))
print('-' * 40)

estoque = (
('Lápis', 1.75),
('Borracha', 2.00),
('Caderno', 15.90),
('Estojo', 25.00),
('Transferidor', 4.20),
('Compasso', 9.99),
('Mochila', 120.32),
('Canetas', 22.30),
('Livro', 34.90),
)
tam = len(estoque)
for i in range(tam):
    print('{:.<30}'.format(estoque[i][0]), end='')
    print('R${:>7.2f}'.format(estoque[i][1]))


print('-' * 40)
