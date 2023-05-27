"""
Modifique as funções que foram ciradas no Exercício 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado po elas vai ser ou não formatado pela função moeda(), desenvolvida no Exercício 108.
"""

from . import moeda
 
p = float(input('Digite o preço: R$'))
print(f'\nA metade de {moeda.moeda(p)} é {moeda.metade(p, True)}.')
print(f'\nO dobro de {moeda.moeda(p)} é {moeda.dobro(p, False)}.')
print(f'\nAumentando 10%, temos {moeda.aumentar(p, 10, True)}.')
print(f'\nReduzindo 13%, temos {moeda.diminuir(p, 13)}.\n')
