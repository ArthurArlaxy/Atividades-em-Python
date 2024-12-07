num=int(input('Digite o Fatorial: '))
c=num
f = 1
print('Calculando {}!'.format(num), end=' -> ')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' =', end=" ")
    f= f * c
    c = c - 1
    
print('{}'.format(f))
