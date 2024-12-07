n1= int(input('Primeiro Valor: '))
n2= int(input('Segunto Valor: '))

opc = 0
while opc != 6:
    opc = int(input('[1]Soma\n[2]Subtração\n[3]Multiplicação\n[4]Maior\n[5]Novos Números\n[6]Sair do Programa\n>>>>>Qual é a sua opção? '))
    if opc == 1:
        print('A soma dos dois números é {}'.format(n1+n2))
    elif opc == 2:
        print('A subtração dos dois número é {}'.format(n1-n2))
    elif opc == 3:
        print('A multiplicação dos dois números é {}'.format(n1*n2))
    elif opc == 4:
        if n1 < n2:
            maior = n2
        elif n1 > n2:
            maior = n1
        print('O maior número é {}'.format(maior)) 
    elif opc == 5 :
        n1 = int(input('Primeiro Valor: '))
        n2 = int(input('Segundo valor: '))
    elif opc == 6:
        0
    else:
        print('Essa opção não existe')
    print(30*'-=')
print(15*'-','Tchauu',15*'-')