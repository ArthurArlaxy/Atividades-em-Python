num=[]
nump=[]
numi=[]

while True:
    n= int(input('Digite um número: '))
    num.append(n)
    if n % 2 == 0 and n not in nump:
        nump.append(n)
    elif n % 2 == 1 and n not in numi:
        numi.append(n)
    while True:
        esc = str(input('Deseja Continuar[S/N]: '))[0]
        if esc in 'Ss':
            break
        elif esc in 'Nn':
            break
        else:
            print('Tente novamente. ',end='')
    if esc in 'Nn':
        break
    esc = ''
print(f'Os números totais adicionados foram {num}')
print(f'Os números pares foram {nump}')
print(f'Os números impares foram {numi}')

