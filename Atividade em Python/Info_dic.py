pessoas= {}
totpessoas = []
idades=[]

print('-='*10,'Cadastros',10*"-=")
f=0
while True:
    pessoas['nome']= str(input('Nome: '))
    pessoas['idade']= int(input('Idade: '))
    i = pessoas['idade']
    while True:
        pessoas['sexo']= str(input('Sexo[F/M]: ')).strip().upper()[0]
        if pessoas ['sexo'] in 'MF':
            if pessoas['sexo'] in 'F':
                f = 1
            break
        else:
            print('ERRO! Responda com M ou F.')
    while True:
        esc= str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
        if esc in 'SN':
            break
        else:
            print('ERRO! Responda com S ou N.')
    totpessoas.append(pessoas.copy())
    idades.append(i)
    del pessoas
    pessoas = {}
    if esc in 'N':
        break
total = len(totpessoas)
media = sum(idades)/total

print('-='*25)
print(f'Ao todo temos {total} pessoas cadastradas')
print(f'A média de idade é de {media:.2f} anos')
if f != 0:
    print(f'As mulheres cadastradas são ',end='')
for i in totpessoas:
    if i['sexo'] == 'F':
        print(i['nome'],end=' ')
print('')
print('A lista de pessoas com idade acima da média é:')
for i in totpessoas:
    if i['idade'] > media:
        for k,v in i.items():
            print(f'{k:>8} = {v:>3}',end='; ')
        print('')
print('-='*25)
print('<<  Encerrado  >>')


