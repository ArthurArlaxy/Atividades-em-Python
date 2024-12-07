opção=str(input('\nDeseja continuar[Sim/Não]: ')).strip().upper()[0]
if opção == 'S':
    termo = int(input('Mais quanto termos deseja saber: '))
    while con-1 != termo:
        con = con + 1
        t3 = t1 + t2
        print(t3,'-> ', end='')
        t1= t2
        t2= t3
    opção=str(input('\nDeseja continuar[Sim/Não]: ')).strip().upper()[0]
else:
    print('Fim')
