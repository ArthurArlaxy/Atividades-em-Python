def fatorial(num=1,show=False):
    """
    Mostra um fatorial de número através de um loop com multiplicação
    num = Receber um número
    
    for c in range(num,0,-1)

        if show :                  \
            if c == 1:              \
                print(c,end=' = ')    > Se show = True --- mostra o cálculo
            else:                   /
                print(c,end=' x ') /

        f*=c  --- é responsavel por fazer o fatorial
    return f  --- Passa o valor para o programa principal
    """
    f = 1
    for c in range(num,0,-1):
        if show :
            if c == 1:
                print(c,end=' = ')
            else:
                print(c,end=' x ')
        f*=c
    return f


print('<<< Calcule o fatorial >>>')
show = bool
while True:
    esc = str(input('Deseja mostrar o calculo[S/N]: ')).strip().upper()[0]
    if esc in 'SN':
        break
    else:
        print('Tente Novamente. ')
num = int(input('Digite um número: '))
if esc in 'N':
    print(f'O fatorial de {num} é {fatorial(num)}')
else:
    print(fatorial(num,show=True))
