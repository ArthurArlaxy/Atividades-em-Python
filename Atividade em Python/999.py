print('Descubra a Soma dos números desejados')
print(50*'-')
cn=0
soma= 0
c = 0
while c != 999:
    cn = cn + 1
    c= int(input('Digite um número(999 para parar): '))
    soma = soma + c 
cn = cn - 1 
soma = soma - 999
print(f'O resultado da soma é {soma}')
print(f'Foram contados {cn} números')
