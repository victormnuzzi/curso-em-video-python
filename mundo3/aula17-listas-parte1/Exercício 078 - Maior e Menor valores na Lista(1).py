# Faça um programa que leia 5 valroes numéricos e guarde-os em uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
lista = []
for i in range(5):
    lista.append(int(input(f'Digite um valor para a Posição {i}: ')))
    maior = max(lista)
    menor = min(lista)
    i_maior = lista.index(max(lista))
    i_menor = lista.index(min(lista))
print(f'O maior valor é {maior} na posição {i_maior} e o menor valor é {menor} na posição {i_menor}.')
