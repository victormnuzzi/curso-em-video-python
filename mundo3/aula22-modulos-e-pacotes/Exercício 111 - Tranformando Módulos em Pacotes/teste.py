"""
Crie um pacote chamado utilidadecev que tenha dois módulos internos chamados moeda e dado.
Transfira todas as funções utilizadas nos Exercícios 107, 108, 109 e 110 para o primeiro pacote e mantenha tudo funcionando.
"""

from ex111.utilidadescev import moeda
 
p = float(input('Digite o preço: R$'))
moeda.resumo(p, 22, 5)
