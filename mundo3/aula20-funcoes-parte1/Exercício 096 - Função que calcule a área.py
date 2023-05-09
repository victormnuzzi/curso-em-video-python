# FUPQ tenha uma função chamada área(), que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a área do terreno.

def area():
    larg = float(input('Largura (m): '))
    comp = float(input('Comprimento (m): '))
    area = larg * comp
    print(f'A área de um terreno {larg}x{comp} é de {area} m2.')


# Programa principal
print('Controle de terreno')
print('-' * 15)

area()
