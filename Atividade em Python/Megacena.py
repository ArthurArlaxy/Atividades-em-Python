from random import randint
from time import sleep

mega=[]
linha=[]

m = 'SIMULE SEUS JOGOS NA MEGA SENA'

print(50*'=')
print(f'{m:^50}')
print(50*'=')
q = int(input('Quantos jogos você quer: '))
l = f'SIMULANDO {q} JOGOS '
print(50*'=')
print(f'{l:^50}')
print(50*'=')
for megas in range(0,q):
    while True:
        n = randint(1,60)
        if n not in linha:
            linha.append(n)
        if len(linha) ==6:
            break
    mega.append(linha[:])
    linha.clear()
    sleep(0.5)
    mega[megas].sort()
    print(f'Jogo {megas}: {mega[megas]}')
print(8* '-=', 'BOA SORTEEE!!!!!', 8*'=-')
