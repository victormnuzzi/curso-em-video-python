# help(print)
# print(input.__doc__)

"""
def contador(i, f, p):
    # tres apas
    -> Faz uma contagem e mostra na tela.
    :param i: início da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return : sem retorno
    Função criada por Victor Nuzzi
    # tres aspas
    c = i
    while c <= f:
        print(f'{c} ', end='')
        c += p
    print('FIM!')

help(contador)
"""
"""
def somar(a=0,b=0,c=0):
    # tres apas
    -> Faz a soma de três valores e mostra o resultado na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    Função criada por Victor Nuzzi
    # tres apas
    s = a + b + c
    print(f'A soma vale {s}.')

somar(3,2,5)
somar(3,2)
somar()

"""

"""
def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1}.')

n1 = 2
funcao()
print(f'N1 fora vale {n1}')
"""

"""
def somar(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 = somar(3,2,5)
r2 = somar(8,10)
r3 = somar(5)
print(f'Os resultados foram {r1}, {r2} e {r3}.')
"""

"""
def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f*=c
    return f

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1}, {f2} e {f3}')

# n = int(input('Digite um número: '))
# print(f'O fatorial de {n} é igual a {fatorial(n)}.')
"""

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    

num = int(input('Digite um número: '))
if par(num):
    print('É par!')
else:
    print('Não é par!')