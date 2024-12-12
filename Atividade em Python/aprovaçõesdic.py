aluno={}
aluno['nome']= str(input('Nome:'))
while True:
    aluno['media']= float(input(f'Média de {aluno["nome"]}:'))
    if aluno['media'] <= 10 and aluno['media'] >=0:
        break
    else:
        print('Tente Novamente. ',end='')

print(f'Nome igual a {aluno["nome"]}')
print(f'Média é igual a {aluno["media"]}')

if aluno['media'] >= 6:
    print(f'{aluno["nome"]} foi aprovada/o')
else:
    print(f'{aluno["nome"]}  foi reprovado/a')