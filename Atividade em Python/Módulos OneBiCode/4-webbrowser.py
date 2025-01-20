import webbrowser

done = False

while not done:
    print('O que deseja fazer?')
    print('1. Aprender Python')
    print('2. Aprender sobre Módulos')
    print('3. Aprender Python, Fullstack JS, Inglês No Code')
    print('4. Sair')

    pick = int(input('>>>'))

    if pick == 1 :
        webbrowser.open('https://www.python.org/')
    elif pick == 2:
        webbrowser.open('https://docs.python.org/3/tutorial/modules.html')
    elif pick == 3:
        webbrowser.open('https://www.youtube.com/@arlaxy6946')
    elif pick == 4:
        done = True
    else:
        print('Opção Invalida')