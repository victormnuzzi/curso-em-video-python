'''Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente
'''
# lista:
valores = []

# while para criar loop infinito ate o usuario dizer que nao quer continuar
while True:
# guardar valo digitado
    valor = int(input('Digite um valor: '))
# cadastrar os valores em uma lista vazia 
# se valor ja existir na lista --> nao cadastrar
    if valor in valores:
        print('Valor duplicado. Não vou adicionar...')
    else:
        print('\nValor cadastrado com sucesso.\n')
        valores.append(valor)
# perguntar se deseja continuar a cadastrar valores
    continuar = input('\nDeseja continuar? [S/N] \n').upper().split()[0]
    
    if continuar == 'N':
# exibir todos os valores unicos digitados em ordem crescente
        print('-='*20)
        if len(valores) > 0:
            print(f'\nVocê digitou os valores {valores}.')
            break
        else:
            print(f'\nVocê digitou o valor {valores}\n')
            break
