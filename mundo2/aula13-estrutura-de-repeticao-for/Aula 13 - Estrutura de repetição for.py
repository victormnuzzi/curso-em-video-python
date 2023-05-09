# for --> Repetir, em loop, X vezes até acabar

#for nome_que_eu_quiser in range(1,3):
#    print('Opa')
#print('Fim')
# Opa, Opa, Fim
# Apenas 2 "Opa", porque não considera o último número no (1,3): 3 -> 2
# Precisa mudar o "1" para "0" --> (0,3)

#for nome_que_eu_quiser in range(5,0, -1): #-1 serve para dizer a interação no fim do laço
#    print(nome_que_eu_quiser)
#print('Fim')
# conta de 5 ate 0 --> 5, 4, 3, 2, 1, 0

#for nome_que_eu_quiser in range(0, 7, 2): # 2 --> conta de 0 até 7 de 2 em 2
#    print(nome_que_eu_quiser)
#print('Fim')
# conta de 2 em 2 --> 0, 2, 4, 6

# n = int(input('Digite um número: '))
#for c in range(0, n + 1): # conta de 0 ate n
#    print(c)
#print('Fim')

# i = int(input('Início: '))
# f = int(input('Fim: '))
# p = int(input('Passo: '))
#for c in range(i, f, p): # conta de i até f de p em p
#    print(c)
#print('Fim')
s = 0
for c in range(0,4):
    n = int(input('Digite um valor: '))
    s += n
print(f'A soma de todos os valores é {s}.')
