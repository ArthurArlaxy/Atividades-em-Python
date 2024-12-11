c=0
res = ''
s = 0
maior = 0
menor = 0
r = 0
while res != 'N':
    c= c + 1
    n  = int(input('Digite um número: '))
    if c == 1:
        maior = menor = n 
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    s = s + n
    res = str(input('Quer continuar[Sim/Não]: ')).strip().upper()[0]
    if res != 'S' and res != 'N' :
        res = str(input('Resposta invalida, deseja continuar?[Sim/Não]: '))
print(f'A soma de todos os valores é {s} e a média foi {s/c}')
print(f'O maior número foi {maior} e o menor foi {menor}')
