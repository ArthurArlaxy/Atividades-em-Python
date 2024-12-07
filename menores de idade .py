from datetime import date
ano = date.today().year
num = 0 
maior = 0
menor =  0
for pessoas in range(0,7,1):
    num = num + 1
    n=int(input('Digite a idade da {}° pessoa'.format(num)))
    idade = ano - n 
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1 
if maior == 0:
    print('Todos são menores de idade')
else:
    if  menor == 0:
        print('Todos são maiores de idade')
    else:
        print('Entre as 7 pessoas descritas {} são menores de idade e {} são maiores de idade'.format(menor,maior))