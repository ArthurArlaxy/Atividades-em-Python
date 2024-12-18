def jogador(Nome='<desconhecido>', Gols=0):
    print(f'O Jogador {Nome} fez {Gols} gol(s) no campeonato')

nome=str(input('Nome do jogador: '))
gols= str(input('Número de gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols=0
if nome.strip() =='':
    jogador(Gols=gols)
else:
    jogador(nome,gols)

