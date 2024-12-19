from utilidadescev.Interface import *
from utilidadescev.arquivo import *
from time import sleep

arq = 'menudecadastro.txt'

if not ArquivoExiste(arq):    
    CriarArquivo(arq)

while True:
    menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do Sistema'])
    num = leiaint('Digite a opção > ')
    if num == 1 :
        texto(f'Pessoas Cadastradas')
        conteudo = lerArquivo(arq)
        sleep(1)
        print(conteudo)
        sleep(3)
    elif num == 2 :
        texto(f'Novo Cadastro')
        nome = str(input('Nome: ')) 
        idade = leiaint('idade: ')
        cadastro = LerCadastro(arq,nome,idade)
    elif num == 3:
        texto('Saindo do Sistema ... tchauuu')
        break
    else:
        print('\033[31mNúmero invalido para opção\033[m')
        sleep(5)
