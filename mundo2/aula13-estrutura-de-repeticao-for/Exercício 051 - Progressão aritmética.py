# Crie um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

print('-=' * 15)
print('10 TERMOS DE UMA P.A')
print('-=' * 15)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))

for c in range(a1, a1 + 10 * r, r):
    print(c, end=' -> ', )
print(f'P.A com o \033[1;36mprimeiro termo\033[m \033[1;32m{a1}\033[m e com \033[1;97mrazão\033[m \033[1;35m{r}\033[m.')
