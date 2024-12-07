print(20*'-','GERADOR DE PA INFINITA',20*'-')
c=0
pt = int(input('Digite o primeiro termo: '))
rz= int(input('Digite a razão: '))
opção = ''
t= 0 
while c != 10:
    t=t + 1
    c = c + 1
    print('{}'.format(pt), ' -> ' if c < 10 else '', end='')
    pt= pt + rz
opção = str(input('\nDeseja continuar[sim/não]: ')).strip().upper()[0]
if opção == 'S':
    c = 0
    n = int(input('Quantos termos a mais você quer mostrar: '))
while opção == 'S':
    while c != n:
        t= t +1
        c = c + 1
        print('{}'.format(pt), ' -> ' if c < n else '', end='')
        pt= pt + rz
    opção = str(input('\nDeseja continuar[sim/não]: ')).strip().upper()[0]
    if opção == 'S':
        n = int(input('Quantos termos a mais você quer mostrar: '))
    c=0
if opção == 'N':
    print(20*'-','Fim da PA',20*'-')
    print('O número de termos pedidos foi {}'.format(t))
