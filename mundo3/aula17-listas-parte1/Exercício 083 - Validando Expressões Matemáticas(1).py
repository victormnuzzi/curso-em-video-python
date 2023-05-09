''' 
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
abertos e fechados na ordem correta.
'''

expr = input('Digite uma expressão: ') # expressao
if expr.count('(') == expr.count(')'):
    print('Expressão correta.')
else:
    print('Expressão incorreta.')
