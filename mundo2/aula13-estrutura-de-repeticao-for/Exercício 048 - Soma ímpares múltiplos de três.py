# Crie um programa que calcule a soma entre todos os números ímpares que são  múltiplos de três e que se encontram no intervalo de 1 até 500.

s = 0
contador = 0
for c in range(1,501):
  if c % 2 == 1 and c % 3 == 0:
    s += c
    contador += 1
print(f'A soma de todos os {contador} valores solicitados é {s}.')
