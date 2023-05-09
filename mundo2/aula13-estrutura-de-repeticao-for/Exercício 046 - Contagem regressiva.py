# Crie um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, 0, -1):
    print(c)
    sleep(1)
print('\033[35mF\033[m\033[34mE\033[m\033[33mL\033[m\033[31mI\033[m\033[32mZ\033[m \033[36mA\033[m\033[97mN\033[m\033[36mO\033[m \033[34mN\033[m\033[32mO\033[m\033[32mV\033[m\033[31mO\033[m!!!!')
