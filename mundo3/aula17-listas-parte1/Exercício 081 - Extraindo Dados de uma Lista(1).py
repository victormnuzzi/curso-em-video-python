''' Crie um programa que vai ler varios numeros e colocar em uma lista. Depois disso mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista. '''

# lista
lista = []
# while loop infinito --> flag vai ser o N
while True:
# ler os numeros e colocar na lista
    n = int(input('Digite um número: '))
    lista.append(n)
    # flag
    resp = str(input('Deseja continuar? [S/N] ')).upper().split()[0]
    # se nao quer continaur
    if resp == 'N':
        lista.sort(reverse=True)
        # A)
        print(f'Você digitou {len(lista)} números.')
        # B)
        print(f'Os valores em ordem decrescente são {lista}.')
        # C)
        if 5 in lista:
            print('O valor 5 faz parte da lista!')
        else:
            print('O valor 5 não faz parte da lsita!')
        break