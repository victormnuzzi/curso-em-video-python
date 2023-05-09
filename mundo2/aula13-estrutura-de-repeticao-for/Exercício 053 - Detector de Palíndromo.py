# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
# Palíndromos --> frases que podem ser lidas de tras pra frente de forma igual

frase = input('Digite uma frase: ').strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1,-1, -1):
    inverso += junto[letra]
print(f'O inverso de \033[35m{junto}\033[m é \033[36m{inverso}\033[m')
if junto == inverso:
    print('\033[32mTemos\033[m um palíndromo.')
else:
    print('\033[31mNão\033[m temos um palíndromo.')
