print('CRIE SUA PIRAMIDE LEFT')

altura = int(input('Qual será a altura da sua piramide: '))
rep = 1
pir= '#'

for i in range(0,altura):
    print(f'{pir * rep}',end='')
    print('')
    rep+=1