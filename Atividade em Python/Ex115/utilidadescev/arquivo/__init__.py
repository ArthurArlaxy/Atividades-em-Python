def ArquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
        return True
    except:
        return False

def CriarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print('Arquivo Criado')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
        conteudo = a.read()
        return conteudo
    except:
        print('O Arquivo não pode ser lido')
    finally:
        a.close()

def LerCadastro(arquivo,nome = '<desconhecido>',idade=0):
    try:
        a = open(arquivo, 'at')
    except:
        print('Tivemos um erro ao tentar abrir o arquivo')
    else:
        try:
            a.write(f'{nome:<25}   \t\t{idade}Anos\n')
            print(f'{nome} foi cadastrado(a).')
        except:
            print(f'Tivemos um erro ao cadastrar {nome}')
    finally:
        a.close()