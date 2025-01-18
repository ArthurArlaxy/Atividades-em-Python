def listar(times):
    for n,time in enumerate(times):
        for nome,elenco in time.items():
            print(f'O time {nome} tem {len(elenco)} jogadores cadastratados e seu indice é {n}')

def addTime():
    listar(times)
    time = input('Digite o nome do time que deseja adicionar: ').strip()
    times.append({time: []})

def removerTime():
    listar(times)
    rem = int(input('Digite o id do time que deseja remover: '))
    if rem < len(times) and rem >=0 :
        times.pop(rem)
        print('Time removido')
    else:
        print('O ID inserido não existe')

def addJogador():
    listar(times)
    id = int(input('Digite o id do time que deseja adicionar o jogador: '))
    if id < len(times) and id >= 0:
        jogador = input('Digite o nome do jogador que deseja adicionar: ').strip()
        nomeTime = list(times[id].keys())[0]
        times[id][nomeTime].append(jogador)
    else:
        print('Time não existe')

def removeJogador():
    listar(times)
    id = int(input('Digite o id do time que deseja remover o jogador: '))
    jogador = input('Digite o nome do jogador que deseja remover: ').strip()
    nomeTime = list(times[id].keys())[0]
    if jogador in times[id][nomeTime]:
        times[id][nomeTime].remove(jogador)
    else:
        print(f'O jogador {jogador} não existe no time {nomeTime}')

def listarJogadores():
    id = int(input('Digite o id do time que deseja saber os jogadores: '))
    if id < len(times) and id >= 0:
        nomeTime = list(times[id].keys())[0]
        print(f'Os jogadores presentes no time {nomeTime} são {times[id][nomeTime]}')
        for n,jogador in enumerate(times[id][nomeTime]):
            print(f'{n}. {jogador}')

times = [
    {'Flamengo': ['Arrascaeta', 'Nico', 'Pedro', 'Cebolinha','beijinho']},
    {'Fluminense': ['Cano', 'John Arias']},
    {'Barcelona': ['Lamine','lewa', 'raphinha']}
]

listar(times)
listarJogadores()