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
    aluno['situação']= 'aprovado'
    print(f'{aluno["nome"]} foi {aluno["situação"]}')
elif aluno['media'] < 6 and aluno['media'] >= 4:
    aluno['situação']= 'Recuperação'
    print(f'O {aluno["nome"]} está em {aluno["situação"]}')
else:
    aluno['situação']= 'reprovado'
    print(f'{aluno["nome"]} foi {aluno["situação"]}')