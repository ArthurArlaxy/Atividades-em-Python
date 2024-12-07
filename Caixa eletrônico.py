print(50*'=')
print('                  BANCO ARLAXY')
print(50*'=')
valor= int(input('Digite o Valor que deseja sacar: '))
total=valor
ced = 100
totalced = 0
while True:
    if total >= ced:
        total = total - ced
        totalced = totalced + 1 
    else:
        break
ced50=50
totalced50=0
while True:
    if total>=50:
        total = total - ced50
        totalced50 = totalced50 + 1
    else:
        break
ced20=20
totalced20=0
while True:
    if total >= ced20:
        total = total - ced20
        totalced20 = totalced20 + 1
    else:
        break
ced10 = 10
totalced10 = 0
while True:
    if total >= 10:
        total = total - ced10
        totalced10 = totalced10 + 1
    else:
        break
ced5 = 5
totalced5 = 0
while True:
    if total >= ced5:
        total = total - ced5
        totalced5 = totalced5 + 1
    else:
        break
ced1 = 1
totalced1 = 0
while True:
    if total >= ced1:
        total= total - ced1
        totalced1 = totalced1 + 1
    else:
        break
if totalced >= 1:
    print('Total de {} cédulas de 100R$'.format(totalced))
if totalced50 >= 1:
    print('Total de {} cédulas de 50R$'.format(totalced50))
if totalced20 >= 1:
    print('Total de {} cédulas de 20R$'.format(totalced20))
if totalced10 >= 1:
    print('Total de {} cédulas de 10R$'.format(totalced10))
if totalced5 >= 1:
    print('Total de {} cédulas de 5R$'.format(totalced5))
if totalced1 >= 1:
    print('Total de {} cédulas de 1R$'.format(totalced1))
print('Volte sempre ao Banco Arlaxy, tenha um bom dia!')
