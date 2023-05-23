def aumentar(preco = 0,taxa = 0):
    res = preco * (1 + taxa/100)
    return res


def diminuir(preco = 0,taxa = 0):
    res = preco * (1 - taxa/100)
    return res


def dobro(preço = 0):
    res = preço * 2
    return res


def metade(preco = 0):
    res = preco / 2
    return res


def moeda(preco = 0, moeda = 'R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')

