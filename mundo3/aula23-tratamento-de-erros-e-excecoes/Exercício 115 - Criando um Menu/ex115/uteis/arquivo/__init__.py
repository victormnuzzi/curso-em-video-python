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