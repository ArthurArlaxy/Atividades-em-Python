from time import sleep

def contagem(inicio , fim, dequanto):
    print('-='*20)
    if dequanto < 0:
        dequanto *=-1
    if dequanto == 0:
        dequanto = 1
        print('0 não tem como,! Faremos de 1 em 1 ')
    if fim < inicio:
        print(f'Contagem de {inicio} a {fim} de {dequanto} em {dequanto}:')
        fim-=1
        if dequanto > 0:
            dequanto = -dequanto
    elif fim > inicio:
        print(f'Contagem de {inicio} a {fim} de {dequanto} em {dequanto}:')
        fim +=1
    for valor in range(inicio,fim,dequanto):
        print(valor,end=' ', flush=True)
        sleep(0.2)
    print('Fim!')


contagem(1,10,1)
contagem(10,0,2)
print('-='*20)
inicio = int(input('Início: '))
fim = int(input('Fim: '))
dequanto = int(input('De quanto em quanto: '))
contagem(inicio,fim,dequanto)