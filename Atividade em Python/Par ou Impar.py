import random
v=0
print(20*'-','PAR OU ÍMPAR GAME',20*'-')
while True:
    comp = random.randint(0,10)
    n = int(input('Digite um número de 1 a 10: '))
    m = str(input('Par ou Ímpar: ')).strip().upper()[0]
    res = n + comp
    if m == 'P':
        if res % 2 == 0:
            print(50*'-','\nVocê venceu\nVocê jogou {} e o computador jogou {}. Total de {} Deu PAR'.format(n,comp,n+comp))
            print('Vamos jogar novamente...')
        else:
            print(50*'-','\nVocê perdeu\nVocê jogou {} e o computador jogou {}. Total de {} Deu ÍMPAR'.format(n,comp,n+comp))
            break
    elif m == 'I':
        if res % 2 == 0:
            print(50*'-','\nVocê perdeu\nVocê jogou {} e o computador jogou {}. Total de {} Deu PAR'.format(n,comp,n+comp))
            break
        else:
            print(50*'-','\nVocê venceu\nVocê jogou {} e o computador jogou {}. Total de {} Deu ÍMPAR'.format(n,comp,n+comp))
            print('Vamos jogar novamente...')
    v= v +1
    print(50*'-')       
print(50*'-')
print('Você teve {} Vítorias'.format(v))