"""
FUPQ tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
Adicione também as docstrings da função.
"""

# Função para armazenar notas de alunos e retornar um dicionário
def notas(*n, sit=False):
    '''
    -> Recebe várias notas e retorna um dicionário
    :param n: As notas da turma
    :param sit: (Opcional) Indica se deve ou não adicionar a situção
    :return: Um dicionário com várias informações sobre a situação da turma
    ''' 
    # declaração das variáveis
    quant, media, maior, menor, situacao = 0, 0, 0, 10, ''

    # verificar a quantidade de notas
    quant = len(n)

    # a função vai criar uma tupla com as notas
    for nota in n: # para cada nota na tupla notas vai adicionar no dicionário
        # verificar qual nota é a maior
        if nota > maior:
            maior = nota
        # verificar qual nota é a maior
        if nota < menor:
            menor = nota
        # calcular a média das notas
        media += nota
    media /= quant

    # calcular situação do aluno com base na média
    if media >= 8.5:
        situacao = 'ÓTIMA'
    if 8.5 > media >= 7.5:
        situacao = 'BOA'
    if 7.5 > media >= 6:
        situacao = 'RAZOÁVEL'
    if 6 > media >= 4.5 :
        situacao = 'RUIM'
    if 4.5 > media:
        situacao = 'MUITO RUIM'

    # adicionando as variáveis no dicionário
    tn = {'total': quant, 'maior': maior, 'menor': menor, 'média': media, 'situação': situacao}
    # verificando se terá a situação
    if not sit: # se sit=False
        del tn['situação'] # apagar a key 'situação'
    return tn



# Programa principal
resp = notas(5.5, 2.5, 8, 10, 5, 2, sit=True)
print()
print(resp)
print()