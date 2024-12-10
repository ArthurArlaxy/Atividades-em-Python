pessoas = []
dados = []
nomep = []
nomel = []
#Salva os inputs de nome e peso na lista pessoas
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    while True:
        esc = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if esc in 'SN':
            break
        else:
            print('Tente novamente. ',end='')
    if esc in 'N':
        break
#Analise ne maior e menor peso       
for c,info in enumerate(pessoas):
    if c == 0:
        maipeso = menpeso = info[1]
        nomep.append(info[0])
        nomel.append(info[0])
    else:
        if info[1] >= maipeso:
            if info[1] != maipeso:
                nomep.clear()
            maipeso = info[1]
            nomep.append(info[0])
        if info[1] <= menpeso:
            if info[1] != menpeso:
                nomel.clear()
            menpeso = info[1]
            nomel.append(info[0])
#decoração de terminal
print(100*'-')
#Informações que sevem ser mostradas
print(f'Voce cadastrou {len(pessoas)} pessoas')            
print(f'O maior peso foi {maipeso:.1f}kg e quem tem esse peso é/são ',end='')
for n in nomep:
    print(f'{n}',end=' ')
print(' ')
print(f'O menor peso foi {menpeso:.1f}kg e quem tem esse peso é/são ',end='')
for n in nomel:
    print(f'{n}',end=' ')