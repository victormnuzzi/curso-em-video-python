"""
Crie um código em Python que teste se o site Pudim está accesível pelo computador usado.
"""

# Minha resolução:
"""
import requests # tive que dar pip install requests

def url_ok(url):
    '''
    -> Verificar se um site está acessível
    :param url: A url digitada pelo usuário
    :return: Se o site está está acessível
    '''
    try:
        status = requests.head(url).status_code
    except:
        return 'O site Pudim não está disponível no momento.'
    else:
        return 'Consegui acessar o site Pudim com sucesso!'
    
    
print(url_ok('http://pudim.com.br/'))
"""

# Resolução do Guanabara

import urllib.request # biblioteca já instalada no python 

def url_ok(url):
    '''
    -> Verificar se um site está acessível
    :param url: A url digitada pelo usuário
    :return: Se o site está está acessível
    '''
    try:
        site = urllib.request.urlopen('http://pudim.com.br/')
    except urllib.error.URLError:
        return 'O site Pudim não está disponível no momento.'
    else:
        return 'Consegui acessar o site Pudim com sucesso!'

    
print(url_ok('http://pudim.com.br/'))