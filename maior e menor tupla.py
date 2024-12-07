from random import randint 
num = (randint(0,9),randint(0,10),randint(0,9),randint(0,9),randint(0,9))
for c in num:
    print(c, end = ' ')
print(end ='\n')
print(f'O maior número sorteado foi {max(num)}')
print(f'O menor número sorteado foi {min(num)}')