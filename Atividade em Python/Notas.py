alunos=[]
dados=[]
soma= []
media =[]
qaluno =[]

print(9*'-=','ANALISADOR DE NOTAS',9*'-=')

nnotas = int(input('Tiveram quantas avaliações esse período:'))

while True:
    n = str(input('Aluno: '))
    dados.append(n)
    for d in range(0,nnotas):
        n = float(input(f'Nota {d+1}: '))
        dados.append(n)
    alunos.append(dados[:])
    dados.clear()
    while True:
        e = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if e in 'NS':
            break
        else:
            print('Tente novamente. ',end='')
    if e == 'N':
        break
for g in range(0,len(alunos)):
    for c,n in enumerate(alunos[g]):
        if c > 0:
            v = n
            soma.append(v)
    m = sum(soma)/nnotas
    media.append(m)
    soma.clear()
print('N°       NOME           MEDIA')
print(50*'=')
for cont in range(0,len(alunos)): 
    print(f'{cont}{alunos[cont][0]:^20}{media[cont]:^12.1f}')
print(50*'=')

for n in range(0,len(alunos)):
    qaluno.append(n)

while True:
    nota = int(input('Deseja mostrar notas de qual aluno(999 para encerrar: '))
    print(50*'-')
    if nota in qaluno:
        print(f'O {alunos[nota][0]} tirou ',end='')
        for c,n in enumerate(alunos[nota]):
            if nota >= 0:
                if c != 0:
                    print(f'[{n}]',end=' ')
        print('')
        print(50*'-')
    elif nota == 999:
        break
    else:
        print('Tente novamente. ',end='')
print('TCHAUU!!!')