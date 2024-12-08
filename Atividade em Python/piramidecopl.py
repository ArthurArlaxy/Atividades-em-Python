print("CRIE SUA PIRAMIDE ")

altura = int(input("Qual é a altura da sua piramide: "))
rep =1

pir = '#'
espaço = altura - rep

for i in range(0,altura):
    espaço = altura - rep
    print(' '* espaço,f'{pir * rep}',end='')
    print(f' {pir * rep}',end='')
    print('')
    rep += 1

