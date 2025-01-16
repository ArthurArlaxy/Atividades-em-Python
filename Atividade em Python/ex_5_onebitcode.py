def upperOrLower(string):
    upper = 0
    lower = 0
    for letter in string:
        if letter == ' ':
            continue
        letra = letter
        letraUpper = letra.upper()
        if letra == letraUpper:
            upper += 1
        else:
            lower += 1
    print(f'Na palavra {string} temos {upper} letras maiúscula(s) e {lower} letras minúscula(s)')

string = input('Digite uma palavra: ')
upperOrLower(string)

def parOrImpar(*num):
    listp = [n for n in num if n % 2 == 0]
    listi = [n for n in num if n % 2 == 1]
    return listp, listi

listanum = []
while True:
    n = int(input('Digite um número para a lista(-1 para parar):'))
    if n == -1:
        break
    else:
        listanum.append(n)

listp, listi = parOrImpar(*listanum)
print(f'Os números pares foram {listp}')
print(f'Os números impares foram {listi}')