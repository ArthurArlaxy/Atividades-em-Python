x = int(input('Digite o número: '))
y = int(input('Digite outro número: '))

soma = x+y

if soma >= 18:
    print('Maior de idade')
else:
    print('Menor de idade')
    pais = input('Você está com seus pais (Sim/Não): ')
    if pais == "Sim":
        print('Pode entrar na festa')
    else:
        print('Não pode entrar na festa')
