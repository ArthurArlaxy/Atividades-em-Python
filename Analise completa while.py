h = 0
m = 0
m20 = 0
idade18 = 0
prox = ''
print(20*'-','CADASTRAMENTO',20*'-')
while True:
    print(20*'=','CADASTRE UMA PESSOA',20*'=')
    sexo = str(input('Digite o sexo[M/F]: ')).strip().upper()[0]
    i = int(input('Digite a idade: '))
    print(50*'-')
    if i > 18:
        idade18 = idade18 + 1
    if sexo == 'M':
        h= h + 1
    if sexo == 'F':
        m = m + 1
        if i < 20:
            m20= m20 + 1
    prox = str(input('Deseja continuar[S/N]: ')).strip().upper()[0]
    if prox == 'N':
        break
    elif prox != 'S':
        prox = str(input('Invalido, Deseja continuar[S/N]: ')).strip().upper()[0]
print('Temos {} maiores de 18 anos'.format(idade18))
print('Temos {} Homens'.format(h))
print('Temos {} Mulheres e {} Mulheres com menos de 20 anos'.format(m,m20))
