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
    tn = dict()
    tn['total'] = len(n)
    tn['maior'] = max(n)
    tn['menor'] = min(n)
    tn['média'] = sum(n) / len(n)

    # verificando se terá a situação
    if sit: # se sit=True
        # calcular situação do aluno com base na média
        # adiciona a key 'situação' e o value "text" ao dicionário
        if tn['média'] >= 8.5:
            tn['situação'] = 'ÓTIMA'
        elif 8.5 > tn['média'] >= 7.5:
            tn['situação'] = 'BOA'
        elif 7.5 > tn['média'] >= 6:
            tn['situação'] = 'RAZOÁVEL'
        elif 6 > tn['média'] >= 4.5 :
            tn['situação'] = 'RUIM'
        elif 4.5 > tn['média']:
            tn['situação'] = 'MUITO RUIM'

    return tn


# Programa principal
resp = notas(5.5, 2.5, 8, 10, 5, 2, sit=True)
print()
print(resp)
print()