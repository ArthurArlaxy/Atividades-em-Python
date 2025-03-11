from time import sleep

frutas = ['Maçã', 'Uva','Banana']
legumes = ['Alface','Pepido','Cebola']
bebidas = ['Cola-Cola','Cerveja','Suco']
carnes = ['Cupim','Peito de Frango','Carré']
outros = ['Vassoura', 'Óleo de Peroba', 'Pano de chão']

while True:
    print('Supermarket Arthur'.center(50,'-'))
    choose = int(input('1 - Frutas\n2 - Legumes\n3 - Bebidas\n4 - Carnes\n5 - Outros\n6 - Sair\nQual opção você deseja: '))
    if choose == 1:
        print(f'Frutas: {frutas}')
        sleep(3)
    elif choose == 2:
        print(f'Legumes: {legumes}')
        sleep(3)
    elif choose == 3:
        print(f'Bebidas: {bebidas}')
        sleep(3)
    elif choose == 4:
        print(f'Carnes: {carnes}')
        sleep(3)
    elif choose == 5:
        print(f'Outros: {outros}')
        sleep(3)
    elif choose == 6:
        print(f'Saindo...')
        sleep(3)
        break
    else:
        print(f'A opção {choose} não existe!')
        sleep(3)