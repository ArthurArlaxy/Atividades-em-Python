exp=[]
x = str(input('Digite a sua expressão: '))
for c in x:
    if c =='(' :
        exp.append(c)
    elif c == ')':
        if 0 != len(exp):
            exp.pop()
        else:
            exp.append(c)
            print('A expressão é invalida')
            break
if len(exp) == 0:
    print('A expressão é valida!!')
