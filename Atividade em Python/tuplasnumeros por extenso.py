números=('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte' )
escolha=''
while escolha != 'N':
    while True:
        num= int(input('Escolha um número de 1 a 20 para ser escrito por extenso: '))
        if num >20:
            print('Esse número é invalido')
        elif num < 0:
            print('Esse número é invalido')
        else:
            break
    print('Você digitou o número',números[num])
    escolha= str(input('Deseja continuar(Sim/Não): ')).strip().upper()[0]
    if escolha != 'N' and escolha != 'S':
        escolha= str(input('Invalido, deseja continuar(Sim/Não): '))
print('Até a proxima!!!!')