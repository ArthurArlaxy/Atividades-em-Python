def texto(msg):
    tam = 4 + len(msg)
    print('~'*tam)
    print(f'{msg:^{tam}}')
    print('~'*tam)

while True:
    texto(str(input('Digite uma frase: ')))
    while True:
        esc = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if esc in 'SN':
            break
        else:
            print('Tente novamente.',end='')
    if esc in 'N':
        break
print('<<<  Encerrado  >>>')