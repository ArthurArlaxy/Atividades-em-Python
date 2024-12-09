num = []
for c in range(0,5):
    n = int(input('Digite um número: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print(f'O valor {n} foi adicionado ao final da lista')
    elif n < num[0]:
        num.insert(0,n)
        print(f'O valor {n} foi adicionado no início da lista')
    else:
        pos=1
        while pos < len(num):
            if n <= num[pos]:
                num.insert(pos,n)
                print(f'O valor {n} foi adicionado na posição {pos}')
                break
            pos+=1
print(90*'=')
print(f'Os valores digitados em ordem foram {num}')