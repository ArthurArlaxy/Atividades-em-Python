num = [[], []]

for c in range(1,8):
    n = int(input(f'Digite o {c}° número: ')) 
    if n %2 == 0 :
        if len(num[0]) == 0 or n >= max(num[0]):
            num[0].append(n)
            print('Número adicionado no final dos pares')
        else:
            pos = 0
            for pos in range(0,len(num[0])):
                if n < num[0][pos]:
                    num[0].insert(pos,n)
                    print(f'Número adicionado na posição {pos} dos pares')
                    break
    else:   
        if len(num[1]) == 0 or n >= max(num[1]):
            num[1].append(n)
            print('Valor adicionado no final dos impares')
        else:
            pos = 0
            for pos in range(0,len(num[1])):
                if n < num[1][pos]:
                    num[1].insert(pos,n)
                    print(f'Número adicionado na posição {pos} dos impares')
                    break
print(f'Os números pares em ordem foram {num[0]}')
print(f'Os números impares em ordem foram {num[1]}')