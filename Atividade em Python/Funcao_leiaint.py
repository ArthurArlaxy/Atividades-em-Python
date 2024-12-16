def leiaint(texto):
    while True:
        n = str(input(texto))
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('\033[0;31mERRO! Digite um número valido.\033[m')
    return n


n = leiaint('Digite um número: ')
print(f'Você digitou o número {n}')