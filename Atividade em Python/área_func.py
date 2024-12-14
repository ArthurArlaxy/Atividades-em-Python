def area(a ,b):
    area = a * b
    print(f'A área de um terreno {a:.2f} X {b:.2f} é de {area:.2f}m²')

print('<<<   Controle de área   >>>')
while True:
    a = float(input('Digite o comprimento(m): '))
    b = float(input('Digite a Largura(m): '))
    area(a,b)
    print('-='*25)
    while True:
        esc = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if esc in 'NS':
            break
        else:
            print('Tente Novamente. ',end='')
    if esc in 'N':
        break
print('-='*25)
print('<<<    ENCERRADO    >>>>')