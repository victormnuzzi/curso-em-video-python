'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar para cada palavra, quais são as suas vogais.
'''
palavras = ('Tesoura', 'Força', 'Luna', 'Terrario', 
'Banheira', 'Rodinha', 'Rato', 'Amor', 'Cachorro',)
vogais = ('a', 'e', 'i', 'o', 'u')

for p in palavras:
    print(f'\nNa palavra {p} temos', end=' ')
    for v in vogais:
        if v in p:
            print(v, end=' ')
