user = "Arlaxy"
password = 'Pedrin'
count = 0
human='S'

while True:
    print('Sistema de Login'.center(50,'-'))

    userInput = input('Digite o usuário: ')
    passwordInput = input('Digite sua senha: ')
    if user == userInput and password == passwordInput and count < 3:
        humanInput = input('Você é humano [S ou N]: ')[0]
        if human == humanInput: 
            print('Você está logado')
            break
        else:
            print('Você não é humano')
    elif count >= 2:
        print('Você excedeu o limite de tentativas')
        break
    else:
        print('Senha ou/e login incorretos')
        count += 1 
        continue