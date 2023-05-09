'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação.
Depois mostre:
A) Os 5 primeiros.
B) Os últimos 4 colocados
C) Times em ordem alfabética.
D) Em que posição está o time da Chapecoense.
'''

brasileirao = ('Atlético Mineiro', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians',
 'Bragantino','Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará SC',
 'Internacional', 'São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 
 'Bahia', 'Sport Recife', 'Chapecoense')
i = brasileirao.index('Chapecoense') 
print(f'\nOs primeiros 5 colocados foram {brasileirao[:5]}\n')
print(f'Os últimos 4 colocados foram {brasileirao[-4:]}\n')
print(f'Os times em ordem alfabética são: {sorted(brasileirao)}\n')
print(f'O time Chapecoense está na posição {i + 1}.')