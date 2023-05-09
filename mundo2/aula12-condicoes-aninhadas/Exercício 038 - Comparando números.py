# Crie um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe alor maior, os dois são iguais

n1 = int(input('Qual é o valor do \033[33mprimeiro numero\033[m? '))
n2 = int(input('Qual é o valor do \033[36msegundo numero\033[m? '))
if n1 > n2:
   print('O \033[33mPRIMEIRO\033[m valor é \033[32mmaior\033[m.')
elif n2 > n1:
   print('O \033[36mSEGUNDO\033[m valor é \033[31mmenor\033[m.')
elif n1 == n2:
   print('Não existe valor \033[32mmaior\033[m, os dois valores são \033[97miguais\033[m.')
