from time import sleep


def l(color,texto):
    print(f'{color}~'*200,'\033[m')
    print(f'{color}{texto:<201}\033[m')
    print(f'{color}~'*200,'\033[m')
def PyHelp():
    while True:
        l('\033[42m','Sistema de ajuda PyHelp')
        ajuda = str(input('Função ou Biblioteca >')).strip().lower()
        if ajuda == 'fim':
            l('\033[45m','Volte sempre que precisar')
            break
        sleep(1)
        l('\033[46m',f'Acessando manual do comando "{ajuda}"')
        sleep(2)
        help(ajuda)  


PyHelp()