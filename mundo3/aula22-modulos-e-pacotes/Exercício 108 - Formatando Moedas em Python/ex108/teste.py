"""
Adapte o código do Exercício 107, criando uma função adicional chamada fmoeda() que consiga mostrar os valores como um valor monetário formatado.
"""

from . import moeda
 
p = float(input('Digite o preço: R$'))
print(f'\nA metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}.')
print(f'\nO dobro de {moeda.moeda(p)} é {moeda.dobro(p)}.')
print(f'\nAumentando 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}.')
print(f'\nReduzindo 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}.\n')