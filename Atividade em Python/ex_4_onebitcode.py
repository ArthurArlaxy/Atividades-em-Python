regres = [x if x != -1 else 'kabom' for x in range(10,-2,-1)]
print(regres)


ini = int(input('Digite o inicio da tabuada: ')) 
fim = int(input('Digite o fim da tabuada: ')) 
num = int(input('Digite o número da tabuada: ')) 
for tab in range(ini, fim):
    print(f'A tabuada de {num} * {tab} = {tab * num}')
print('fim')