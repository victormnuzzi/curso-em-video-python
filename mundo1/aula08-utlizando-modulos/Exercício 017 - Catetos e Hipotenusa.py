#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo, calcule e mostre o seu comprimento da hipotenusa.
#nao sabia da hypot
from math import hypot
co = float(input('Qual é o cateto oposto? '))
ca = float(input('Qual é o cateto adjacente? '))
hi = hypot(co,ca)
print(f'O comprimento da hipotenusa é {hi}.')