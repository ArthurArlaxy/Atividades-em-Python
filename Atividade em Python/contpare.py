pares = int(input('Quantos pares você deseja encontrar? '))
for c in range(0, 2*pares, 2):
    print (c, end='-> ')
print('acabou')

ate_pares = int(input('Você deseja saber quais são os números pares ate aonde? '))
for atep in range(0,ate_pares,2):
    print(atep, end=' -> ')
print('acabou')