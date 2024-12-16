from random import randint
from time import sleep

def sorteio():
    print('Sorteando os valores da lista ',end='',flush=True)
    sleep(0.5)
    for c in range(0,5):
        n = randint(1,10)
        num.append(n)
        sleep(0.4)
        print(f'{n} ',end='',flush=True)
    print('pronto!')
def pares(num=[]):
    sleep(0.5 )
    soma=0
    for c in num:
        if c %2 == 0:
            soma += c
    print(f'Somando os valores pares de {num}, temos {soma}')

help(num) 
sorteio()
pares(num)
