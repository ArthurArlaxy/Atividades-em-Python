valores=[9]
valores.append(8)
valores.append(4)
for cont in range(0,3):
    valores.append(int(input("Digite os novos valores: ")))
print(valores)
for pos,v in enumerate(valores):
    print(f'Na posição {pos} o valor é {v}!')
print(f'A acabei a contagem da lista com os valores ', end='')
for v in valores:
    print(f'{v}',end=' ')
