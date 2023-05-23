def aumentar(preco=0, taxa=0, formato=False):
    res = preco * (1 + taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preco=0, taxa=0, formato=False):
    res = preco * (1 - taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    res = preço * 2
    return res if formato is False else moeda(res)


def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.',',')


def resumo(preco=0, taxaa=10, taxar=5):
    print('-'*36)
    print('RESUMO DO VALOR'.center(36))
    print('-'*36)
    print(f'Preço analisado: \t{moeda(preco)}')
    print(f'Dobro do preço: \t{dobro(preco, True)}')
    print(f'Metade do preço: \t{metade(preco, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(preco, taxaa, True)}')
    print(f'{taxar}% de redução: \t\t{diminuir(preco, taxar, False)}')
    print('-'*36)

