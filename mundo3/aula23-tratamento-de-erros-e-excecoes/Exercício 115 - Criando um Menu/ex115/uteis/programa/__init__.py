from time import sleep
from ex115.uteis import verificacao
from ex115.uteis import estetica

def sistema():
    status = 1 # ligado
    while status != 0: # enquanto status nõa for desligado
        # Print Menu Principal e Opções
        estetica.titulo('MENU PRINCIPAL', '=')
        quant_opcoes = estetica.menuOpcoes('Ver pessoas cadastradas', 'Cadastrar nova Pessoa', 'Sair do Sistema') # quant_opcoes do menu opções

        # Loop da escolha da opção
        escolha = verificacao.vOpcao(quant_opcoes)
        estetica.titulo(f'OPÇÃO {escolha}', '-')
        match escolha:
            case 1:
                break
            case 2:
                
                break
            case 3:
                status = 0
            
    else:
        print('Saindo do programa...')