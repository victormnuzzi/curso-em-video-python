#Crie um programa que faça o computador "pensar" um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5...')
print('-=-' * 20)
n = int(input('Em que número eu pensei? '))
if n > 5 or n < 0:
    print('Erro. O seu número deve estar entre 0 e 5.')
else:
    s = random.randint(0, 5)
    print('Parabéns, você GANHOU! Você acertou o número!' if n == s else 'Não foi dessa vez...Você PERDEU!')
    print(s)
