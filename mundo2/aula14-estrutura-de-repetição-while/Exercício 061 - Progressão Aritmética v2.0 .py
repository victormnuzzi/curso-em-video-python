print('-=' * 16)
print('     10 TERMOS DE UMA P.A')
print('-=' * 16)
a1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
n = 0
#print(a1, end=' -> ')
#for i in range(1,10):
#    n += 1
#    an = a1 + n * r

#    print(an, end=' -> ')
#print('FIM')

print(a1, end=' -> ')
while n != 9:
    n += 1
    an = a1 + n * r
    print(an, end=' -> ')
print('FIM')