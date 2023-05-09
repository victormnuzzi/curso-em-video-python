# Crie um programa que elia a velocidade de um carro. Se ele ultrapssar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.

v = int(input('Qual é a velocidade do carro? '))
m = (v - 80) * 7
if m >= 1:
    print(f'Você está acima do limite de velocidade! Você foi multado e deverá pagar R${m:.2f}.')
elif m <= 0:
    print('Cuidado! Você está no limite de velocidade.')
else:
    print('Você está abaixo do limite de velocidade.')
print('Tenha um bom dia!')
