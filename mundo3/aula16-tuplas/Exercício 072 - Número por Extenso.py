'''
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

valores = ('zero','um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze',
'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete','dezoito', 'dezenove', 'vinte')

while True:
    v = int(input('Digite um número entre 0 e 20: '))
    if 0 <= v <= 20:
        print(f'Você digitou o número {valores[v]}.')
        break
    else:
        print('Tente Novamente. ', end='')
    


