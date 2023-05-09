# Crie um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
# O programa será interrompido quando o número solicitado for negativo


v = cont = 0
while True:
    v = int(input('Quer saber a tabuada de qual valor? '))
    print('=' * 40)
    cont = 0
    if v <= 0:
        print('\033[31mGERADOR DE TABUADA ENCERRADO.\033[m')
        break
    while cont < 10:
        cont += 1
        print(f'{v} x {cont} = {v * cont}')
    print('=' * 40)
