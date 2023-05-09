''' Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, 
já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela. '''

# lista
lista = []

# for pois tem range definido
for v in range(0,5):

    # cadastrar os 5 valores
    num = int(input('\nDigite um valor: '))

    # se for o primeiro valor ou se o número for maior que o ultimo valor da lista --> vai adicionar no final da lista
    if v == 0 or num > lista[-1]:
        lista.append(num)
        print('Adicionado no final da lista.')

    # se nao for nenhuma dessas condicoes:
    else: 
        i = 0  # indice começa no 0 --> vai passar por todos os valores dentro da lista
        while i < len(lista):  # enquanto o indice for menor do que os indices da lista
            if num < lista[i]:  # se o valor for menor do valor do indice i, adicionar o valor no indice i
                lista.insert(i, num)
                print(f'Adicionado na posição {i}.')
                break
            i += 1
print(lista)