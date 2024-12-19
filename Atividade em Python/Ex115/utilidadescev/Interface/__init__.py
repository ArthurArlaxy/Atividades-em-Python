def texto(texto):
    print('-'*50)
    print(f'{texto:^50}')
    print('-'*50)

def leiaint(dado):
    while True:
        try:    
            r = int(input(f'{dado}'))
        except KeyboardInterrupt:
            print('\033[31mNão digitou nada\033[m')
            return 'nenhum'
        except:
            print(f'\033[31mErro!não é uma opção valida\033[m')
        else:
            return r

def menu(lista=[]):
    texto('Menu Principal')
    c = 1
    for opção in lista:
        print(f'\033[34m{c}\033[m - \033[36m{opção}\033[m')
        c+=1
    print('-'*50)
