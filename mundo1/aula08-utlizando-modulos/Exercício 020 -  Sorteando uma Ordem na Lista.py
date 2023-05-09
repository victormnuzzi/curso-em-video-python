#O professor quer sortear a ordem de apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1 = str(input('Primeiro: '))
a2 = str(input('Segundo: '))
a3 = str(input('Terceiro: '))
a4 = str(input('Quarto: '))
lista = [a1, a2, a3, a4]
random.shuffle(lista)
print(f'A ordem dos alunos é {lista}')
