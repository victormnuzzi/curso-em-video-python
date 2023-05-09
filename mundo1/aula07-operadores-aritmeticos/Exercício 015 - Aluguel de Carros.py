#Faça um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Informe a quantidade de Km percorridos pelo carro: '))
dias = int(input('Informe a quantidade de dias pelos quais ele foi alugado: '))
preço = (dias * 60) + (km * 0.15)
print(f'O preço a pagar pelo carro é de {preço:.2f}.')