from random import randint

print(f'Bem vindo ao jogo do número secreto'.center(100,'-'))
quero = True

while quero:
    numeroSecreto = randint(1,100)
    while True:
        while True:
            chute = input('Digite o número: ')
            try:
                chute = int(chute)
                break
            except:
                print('Valor invalido',end='')
        if chute == numeroSecreto:
            print('Parabens!!! Você acertou')
            esc = input('Deseja continuar(s/n): ').strip().lower()[0]
            if esc == 's':
                break
            else:
                quero = False
                break
        else:
            if chute > numeroSecreto:
                print(f'O número secreto é menor que {chute}')
            else:
                print(f'O número secreto é maior que {chute}')
print(f'Obrigado por participar')
