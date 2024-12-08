palavras=('carros','porta','namorado','cachorro','notebook','pneus','formula','laudo')

for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ',end='')
    for letra in p:
        if letra.upper() in 'AEIOU':
            print(f'{letra.upper()}',end=' ')