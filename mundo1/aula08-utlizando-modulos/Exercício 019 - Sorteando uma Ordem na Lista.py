#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo os nome deles e escrevendo o nome do escolhido.
import random
a1 = input('Primeiro aluno: ')
a2 = input('Segundo aluno: ')
a3 = input('Terceiro aluno: ')
a4 = input('Quarto aluno: ')
lista = [a1, a2, a3, a4]
sorteio = random.choice(lista)
print(f'O aluno escolhido foi o {sorteio}.')
