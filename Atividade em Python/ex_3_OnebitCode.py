print('Calcule o preço da viagem'.center(50, '-'))

km = float(input('Digite a Distancia da Viagem: '))

if km <= 200 and km >= 0:
    preco = km * 0.5
elif km > 200:
    preco = 100 + (km - 200) *0.35
else:
    print('Distancia Invalida')

print(f'O preço da passagem foi de {preco:.2f}')

print('Calcule seu aumento'.center(50,'-'))

salario = float(input('Digite seu salário: '))

if salario <= 1250.00:
    if salario > 0:
        novoSalario = salario + salario * 0.15
    else:
        print('Salário invalido')
        novoSalario = 0
if salario > 1250.00:
    novoSalario = salario + salario * 0.1

print(f'Seu novo salário é {novoSalario:.2f}')