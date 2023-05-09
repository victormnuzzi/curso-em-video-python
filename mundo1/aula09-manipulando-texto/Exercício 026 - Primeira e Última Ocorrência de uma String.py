#Crie um programa que leia uma frase pelo teclado e mostre: 1) Quantas vezes aparece a letra "A"; 2) Em q posição "A" aparece na primeira e na última vez
frase = input('Digite uma frase: ').lower()
v = frase.count('a')
p = frase.find('a')+1
u = frase.rfind('a')+1
print(f'1) A letra "A" aparece {v} vezes. \n 2) A primeira letra "A" aparece na posição {p}. \n 3) A última aparece na posição {u}.')
