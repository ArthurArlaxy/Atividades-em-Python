c = 0
s = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    c= c + 1
    s = s + n
print(f'Você somou {c} números e a soma de todos os números é {s}')
