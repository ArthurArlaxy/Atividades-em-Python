from random import randint

num = (randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('O Números sorteados foram: ',end='')
for n in num:
    print(n, end=' ')
print(f'\nO maior valor presente na tupla é {max(num)}')
print(f'O menor valor presente na tupla é {min(num)}')