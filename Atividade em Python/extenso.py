numbers = ('zero','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen' ,'twenty')

while True:
    escolha= int(input("Que número vc quer por extenso em ingles(0 a 20): "))
    while True:
        if escolha >= 0 and escolha <=20:
            break
        else:
            escolha= int(input("Tente Novamente. Que número vc quer por extenso em ingles(0 a 20): "))
    print(f'O numero é {numbers[escolha]}')
    next = str(input('Gostaria de continuar(S/N): ')).strip().upper()[0]
    while True:
        if next in 'S' or next in 'N':
            break
        else:
                next = str(input('Tente novamente, Deseja Continuar(S/N): ')).strip().upper()[0]
    if next == 'S':
        continue
    else:
        break
print('TCHAUUU!!!!')
