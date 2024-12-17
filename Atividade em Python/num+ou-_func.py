from time import sleep

def infos(num=[]):
    print('-='*25)
    sleep(0.5)
    print(f'Analizando os valores {num}')
    sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo')
    sleep(0.5)
    print(f'O maior valor foi {max(num)} e o menor foi {min(num)} e a soma de todos eles foi {sum(num)}')
    print('-='*25)

num = []
while True:
    while True:
        n= int(input('Digite um número: '))
        num.append(n)
        while True:
            esc = str(input('Deseja continuar adicionando números[S/N]: ')).strip().upper()[0]
            if esc in 'NS':
                break
            else:
                print('Tente novamente. ',end='')
        if esc in 'N':
            break
    infos(num)
    num =[]
    while True:
        prom = str(input('Deseja encerrar o programa[S/N]: ')).strip().upper()[0]
        if prom in "NS":
            break
        else:
            print('Tente Novamente. ',end='')
    if prom in 'S':
        break
print('-='*25)
print('<<<  Encerrado  >>>')
