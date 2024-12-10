matriz = []

for i in range(0,3):
    for c in range(0,3):
        matriz.append(int(input(f'Digite um número para a posição [{i}, {c}]: ')))
print(100*'=')
for c,m in enumerate(matriz):
    print(f'[ {m:^5} ]',end='')
    c += 1
    if c % 3 == 0 and c != 0:
        print('')
    c-=1