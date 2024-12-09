num=[]
n5=0
while True:
    n = int(input('Digite um número: '))
    num.append(n)
    if n == 5:
        n5+=1
    escolha = str(input('Deseja continuar [S/N]: '))
    if escolha in 'Ss':
        continue
    elif escolha in 'Nn':
        break
    else:
        escolha= str(input('Tente novamente. Deseja continuar [S/N]: '))
    if escolha in 'Nn':
        break
num.sort(reverse=True)
print(f'A Lista que você criou tem {len(num)} números')
print(f"A Lista em ordem decrescente é {num}")
if 5 in num:
    print(f'O 5 está presente na lista, apareceu em {n5} momento(s)')
else:
    print('O número 5 não apareceu na lista')