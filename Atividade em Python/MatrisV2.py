matriz =[[0 , 0 , 0],[0, 0, 0],[0 ,0, 0]]

for l in range(0,3):
    for m in range(0,3):
        matriz[l][m] = int(input(f'Digite um número para [{l+1}, {m+1}]:'))
print('='*100)
print(f'{'SUA MATRIZ FOI':^100}')
for l in range(0,3):
    print('')
    for m in range (0,3):
        print(f'[{m:^5}]',end=' ')
