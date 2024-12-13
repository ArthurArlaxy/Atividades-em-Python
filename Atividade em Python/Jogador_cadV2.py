print('===              CADASTRO DE JOGADOR                ===')
jogador = {}
gols=[]
time=[]
while True:
    jogador['nome'] = str(input('Qual é o nome do jogador: '))
    jogos = int(input('Quantos jogos ele tem no campeonato: '))
    for c in range(0,jogos):
        gol = int(input(f'Quantos gols ele marcou na partida {c+1}: '))
        gols.append(gol)
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    time.append(jogador.copy())
    gols.clear()
    jogador.clear()
    while True:
        esc = str(input('Deseja continuar[S/N];')).strip().upper()[0]
        if esc in 'SN':
            break
        else:
            print('Tente Novamente. ')
    if esc in 'N':
        break
print('-='*25)
print('Id  Nome          Gols       total')
print('-'*50)
for c,i in enumerate(time):
    print(f'{c} ',end='')
    for v in i.values():
        print(f'{str(v):<15}',end='')
    print()

while True:
    while True:
        print('-'*50)
        jogador_escolhido = int(input('Deseja levantar os dados de qual jogador(-1 para parar): '))
        if jogador_escolhido > len(time) -1 or jogador_escolhido < -1:
            print(f'ERRO! Não existe jogador com código {jogador_escolhido} ',)
        elif jogador_escolhido == -1:
            break
        else:
            print(f'-- Levantamento do jogador {time[jogador_escolhido]["nome"]}:')
            for c,i in enumerate(time[jogador_escolhido]["gols"]):
                print(f'     No jogo {c+1} ele fez {i}')
            print(f'Foi um total de {time[jogador_escolhido]["total"]} gols')

    if jogador_escolhido == -1:
        break
        
