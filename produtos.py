n= 0
r= 0
valor=0
menor = 0
barato = ''
md =0
c = 'S'
while c == 'S':
    n = n + 1
    p = str((input('Digite o Nome do produto: ')))
    r= float(input('Digite o valor do produto: R$'))
    valor = valor + r 
    if n == 1:
        menor = r
        barato = p
    else:
        if r < menor:
            menor = r
            barato = p
    if r > 1000:
        md = md + 1
    c = str(input('Deseja continuar: ')).strip().upper()[0]
    if c == 'N':
        break
    elif c == 'S':
        continue
    else:
        c = str(input('Invalido, Deseja continuar: '))
print('O valor total dos produtos foi {}'.format(valor))
print('O produto mais barato foi {} por {}R$'.format(barato,menor))
print('Tem {} que custa mais de 1000R$'.format(md))
