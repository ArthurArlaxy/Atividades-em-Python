from random import randint
from time import sleep

jogadores = {}
jogadas = []
nj = int(input('Qual é o número de jogadores: '))
for c in range(nj):
    jogadores['nome'] = str(input(f'Jogador {c+1}: '))
    jogadores['dado'] = randint(1,6)
    for i in range(3,0,-1):
        sleep(0.5)
        print(f'{i}!!')
    print(f'O número do dado foi {jogadores["dado"]}')
    jogadas.append(jogadores.copy())

# Ordenar jogadas por valor do dado de forma decrescente
jogadas_ordenadas = sorted(jogadas, key=lambda x: x['dado'], reverse=True)

print('-='*25)
print("====    Ranking dos Jogadores   ====")
for c,jogador in enumerate(jogadas_ordenadas):
    sleep(0.5)
    print(f"{c+1}° - {jogador['nome']:5} tirou {jogador['dado']}")
