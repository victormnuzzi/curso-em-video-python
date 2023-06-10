from ex115.uteis import interface

def createF(name=''):
    """
    -> Cria um arquivo txt e se já existir
    :param name: Nome do arquivo
    """
    try:
        file = open(name, "x")        
        print(f"O arquivo {name} foi criado com sucesso!")
    except:
        print('', end='')
        

def readF(name=''):
    """
    -> Lê um arquivo txt w printa o conteúdo dele
    """
    fileR = open(name, "rt")
    print(fileR.read())


def appendF(name=''):
    """
    -> Adiciona o nome e a idade da pessoa que será cadastrada
    :param name: Nome do arquivo
    """
    fileA = open(name, "a") # adicionar texto no arquivo txt
    pessoa = [] # lista da pessoa
    nome = input('Nome: ') # nome
    idade = input('Idade: ') # idade
    tam_espaco = interface.tamPrograma() - len(nome) - len(f'{idade} anos') - 2 # tamanho do espaço entre nome e idade
    pessoa.append(f' {nome}')
    pessoa.append(' ' * tam_espaco)
    pessoa.append(f'{idade} anos\n')
    try:
        fileA.writelines(pessoa)
        print(f'Novo registro de {nome} adicionado.')
    except:
        print('ERRO! Não foi possível cadastrar essa pessoa.')
    