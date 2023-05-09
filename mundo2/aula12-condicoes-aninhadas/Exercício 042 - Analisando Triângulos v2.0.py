# Refaça o EX 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)

r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento: '))
r3 = float(input('Terceiro segmento: '))

if r1 == r2 == r3:
    t = 'equilátero'
elif r2 == r1 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
    t = 'isósceles'
else:
    t = 'escaleno'
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print(f'Essas segmentos podem formar um triângulo {t}!')
else:
    print('Essas segmentos não podem formar um triângulo!')
