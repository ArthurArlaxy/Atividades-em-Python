print('PIRAMIDE RIGHT')

altura= int(input('Digite qual será a altura da piramide: '))
rep=1

pir='#'

for hash in range(0,altura):
    espaco = altura - rep
    print(' ' * espaco ,f'{pir * rep}', end='')
    print('')
    rep+=1