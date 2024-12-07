n = 1
pares = []
impares = []
while n != 0:
    n= int(input('Digite um número:'))
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print('Tiveram {} números pares e {} números impares'.format(len(pares),len(impares)))
print('Os números pares são',pares)
print('Os números impares são',impares)
