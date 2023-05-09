'''FUPQ tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.
Ex: escreva("Olá, Mundo!")
Saída: 
~~~~~~~~~~~~
Olá, Mundo!
~~~~~~~~~~~~
'''

def escreva(texto):
    tam = (len(texto) + 8)
    print('~' * tam)
    print(f'{texto:^{tam}}')
    print('~' * tam)

# Programa principal
escreva('Victor Marcondes Nuzzi')
escreva('Curso de Pyhton')
escreva('nuzzi')