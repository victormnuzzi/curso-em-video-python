"""
Reescreva a função leiaInt() (do exercício 104), incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade
"""

# Exercício 104:
"""
    FUPQ tenha uma função leiaInt(), que vai funcionar de semelhante à função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
    Ex: n = leiaInt('Digite um n)
"""

# Programa principal

from ex113 import dados

n_int = dados.leiaInt('Digite um número inteiro: ') # chamando a função
n_float = dados.leiaFloat('Digite um número real: ')
print(f'Você digitou o número inteiro {n_int} e o número float {n_float}.') # print final
