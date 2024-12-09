exp=[]
x = str(input('Digite a sua expressão: '))
for c in x:
    if c in'({[' :
        exp.append(c)
    elif c in ')}]':
        if 0 != len(exp):
            exp.pop()
        else:
            print('A expressão é invalida')
            break
    if len(exp) == 0:
        print('A expressão  é valida!!')
