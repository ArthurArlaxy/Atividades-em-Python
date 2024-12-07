import random
print('Acabei de pensar em um número, será que você consegue acertar?')
num= random.randint(0,10)
seun = 11
palpites = 0
while seun != num:
    palpites = palpites + 1
    seun = int(input('Escolha um número de 0 a 10: '))
    if seun < num:
        print('Número baixo,tente novamente')
    elif seun > num:
        print('Você passou do número, tente novamente')
print(15*'-','PARABENS',15*'-')
print('Isso a maquina escolheu o número {}'.format(num))
print('Você tentou {} vezes antes de acertar'.format(palpites))
