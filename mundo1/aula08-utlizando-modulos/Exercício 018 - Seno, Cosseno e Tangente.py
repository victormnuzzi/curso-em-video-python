#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import tan, cos, sin, radians
ang = int(input('Digite o ângulo: '))
s = sin(radians(ang))
c = cos(radians(ang))
tg = tan(radians(ang))
print(f'O ângulo {ang} tem como seno {s:.2f}, cosseno {c:.2f} e tangente {tg:.2f}.')