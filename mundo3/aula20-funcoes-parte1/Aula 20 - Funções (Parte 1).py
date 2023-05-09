'''
def lin1():
    print('-=' * 15)

    
# Programa principal
lin1()
print('Sistema de alunos')
lin1()

lin1()
print('ERRO')
lin1()

lin1()
print('Menu')
lin1()

'''
'''
def lin2(titulo):
    print('-=-' * 10)
    print(f'{titulo:^30}')
    print('-=-' * 10)
    print('\n')


# Programa principal
lin2('Sistema de alunos')

lin2('ERRO')

lin2('Menu')
'''

'''
# Esse código se repete 3 vezes
a = 4 
b = 5
s = a + b
print(s)

a = 1 
b = 3
s = a + b
print(s)

a = 2 
b = 6
s = a + b
print(s)
'''

'''
def soma(a, b):
    s = a + b
    print(s)


# Programa principal
soma(4, 5)
soma(1, 3)
soma(2, 6)
soma(b=4, a=1)
'''

'''
def contador(*num):
    print(num)


# Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
'''
def contador(*num):
    for valor in num:
        print(f'{valor} ', end='')
    print('FIM')


# Programa principal
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
'''
'''
def dobra(lista):
    posicao = 0
    while posicao < len(lista):
        lista[posicao] *= 2
        posicao += 1


# Programa principal
valores = [6, 3, 9, 1, 0, 2]
print(valores)
dobra(valores)
print(valores)
'''

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}.')



# Programa principal
soma(5, 2)
soma(2, 9, 4)
