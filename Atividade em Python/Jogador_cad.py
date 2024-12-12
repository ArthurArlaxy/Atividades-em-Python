print('===              CADASTRO DE JOGADOR                ===')
jogador = {}
gols=[]
jogador['nome'] = str(input('Qual é o nome do jogador: '))
jogos = int(input('Quantos jogos ele tem no campeonato: '))
for c in range(0,jogos):
    gol = int(input(f'Quantos gols ele marcou na partida {c+1}: '))
    gols.append(gol)
jogador['gols'] = gols[:]
jogador['total'] = sum(gols)
print('-='*25)
print(jogador)
print('-='*25)
for k,v in jogador.items():
    print(f'A chave "{k}" tem valor {v}')
print('-='*25)
print(f'O jogador {jogador["nome"]} jogou {jogos} partidas')
for c in range(0,jogos):
    print(f'-> Na partida {c+1} ele fez {jogador["gols"][c]} gols.')
print(f'Total de {jogador["total"]}')