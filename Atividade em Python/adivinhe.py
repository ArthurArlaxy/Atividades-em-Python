from random import randint

while True:
    num = randint(1,3)
    my= int(input('Escolha um número: '))
    

    if num == my :
        print('Você adivinhou!!!')
        want = int(input('Do you want to play again? \n[1]yes \n[2]No\nAnswer: '))
        if want == 1:
            continue
        else:
            break
    else:
        print('O número era 3 Errou tente novamente!!'.format (num))
print('Muito obrigado por jogar, tchauuu!')