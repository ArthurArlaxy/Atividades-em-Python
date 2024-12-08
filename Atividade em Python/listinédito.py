num =[int(input('Digite um número: '))]


while True:
    escolha = str(input('Deseja Continuar (S/N): ')).strip().upper()[0]
    if escolha == 'S':
        n = int(input('Digite um número: '))
        if n not in num:
            num.append(n)
    elif escolha == 'N':
        break
    else:
        print('Tente novamente.',end="")

print(num)