matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for m in range(0,3):
        matriz[l][m]=int(input(f'Digite o número para [{l+1}, {m+1}]: '))
print('='*100)
print(f'{"MATRIZ V3":^100}')
for l in range(0,3):
    print('')
    for m in matriz[l]:
        print(f"[{m:^5}]",end='')
print(f'\nA soma da primeira linha foi {sum(matriz[0])}')
print(f'O maior número da linha 2 foi {max(matriz[1])}')
print(f'A soma da coluna 3 foi {matriz[0][2]+matriz[1][2]+matriz[2][2]}')
