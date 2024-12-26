num =[int(input('Digite um número: '))]
print('Valor foi adicionado')

while True:
    escolha = str(input('Deseja Continuar (S/N): ')).strip().upper()[0]
    if escolha == 'S':
        n = int(input('Digite um número: '))
        if n not in num:
            num.append(n)
            print('Valor foi adicionado')
        else:
            print('Valor repetido, não será adicionado')
    elif escolha == 'N':
        break
    else:
        print('Tente novamente.',end="")
print(20*'=-')
num.sort()
print(f'Os números inéditos foram {num}')