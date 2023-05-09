# Refaça o Exercício 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.
s = 0
n = int(input('Digite um número: '))
for c in range(1, 11):
    s += n
    print(f'{n} x {c} = {s}')
print('Fim.')