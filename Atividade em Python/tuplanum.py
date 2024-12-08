a = int(input('Digite um número: '))
b= int(input('Digite um número: '))
c= int(input('Digite um número: '))
d= int(input('Digite um número: '))

num= (a,b,c,d)

pares = [numeros for numeros in num if numeros % 2 == 0]

print(num)

print(f'O número 9 apereceu {num.count(9)} vezes')
if 3 in num:
    print(f'O primeiro valor 3 foi digitado na posição {num.index(3) + 1}')
else:
    print('O número 3 não foi digitado')
print(f'Os números pares digitado foram {pares}')