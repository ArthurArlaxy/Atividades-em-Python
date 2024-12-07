c=0
while True:
    c=0
    n= int(input('Digite um número para saber a Tabuada (Negativo para parar): '))
    if n < 0:
        break
    while c != 10:
        c= c + 1
        print('{} X {} = {}'.format(n,c,n*c))
print(50*'-')
print('Tchau')