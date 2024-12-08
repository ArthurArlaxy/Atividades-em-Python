num =[int(input('Digite um número: '))]
n=0

while True:
    escolha = str(input('Deseja Continuar (S/N): ')).strip().upper()[0]
    if escolha == 'S':
        num.append((int(input('Digite um número: '))))
        n+=1
        l = num[n]
        if l in num[1-n]:
            num.pop()
    elif escolha == 'N':
        break
    else:
        print('Tente novamente.',end="")

print(num)