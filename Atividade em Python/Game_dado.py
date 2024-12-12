from random import randint
from time import sleep
from operator import itemgetter

jogo = {
    'Jogador 1': randint(0,6),
    'Jogador 2': randint(0,6),
    'Jogador 3': randint(0,6),
    'Jogador 4': randint(0,6)}
for k,v in jogo.items():
    sleep(1)
    print(f'O {k} tirou {v} no dado')
print('-='*25)
rank = []
rank = sorted(jogo.items(), key=itemgetter(1), reverse=True)
print('                == Ranking ==')
for k,v in enumerate(rank):
    sleep(1)
    print(f'{k+1}° {v[0]} que tirou {v[1]}')