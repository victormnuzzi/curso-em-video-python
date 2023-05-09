# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
# - Abaixo de 18.5: Abaixo do Peso
# - Entre 18.5 e 25: Peso ideal
# - 25 a 30: Sobrepeso
# - 30 a 40: Obesidade
# - Acima de 40: Obesidade mórbida

peso = float(input('Qual é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
IMC = peso / altura**2
if IMC < 18.5:
    status = '\033[1;31mabaixo do peso normal\033[m.'
elif 18.5 < IMC < 25:
    status = 'com\033[1;32m peso ideal\033[m.'
elif 25 < IMC < 30:
    status = 'em \033[1;33msobrepeso\033[m.'
elif 30 < IMC < 40:
    status = 'em \033[1;31mobesidade!\033[m.'
else:
    status = 'em\033[1;31mobesidade mórbida\033[m, cuidado!!'
print(f'O seu IMC é \033[36m{IMC:.0f}\033[m e você está {status}')