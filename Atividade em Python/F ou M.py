n = ''
while n != 'M' and n != 'F':
    n= str(input('Digite o sexo:')).strip().upper()[0]
    if n != 'M' and n != 'F':
        print('Invalido')
if n == 'M':
    print(30*'-')
    print('O Sexo masculino foi definido')
if n == 'F':
    print(30*'-')
    print('O Sexo Femenino foi definido') 