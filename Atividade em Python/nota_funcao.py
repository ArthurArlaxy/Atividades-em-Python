def nota(*num,sit=False):
    lista = list(num)
    resp = {
        'Total': len(lista),
        'Maior': max(lista),
        'Menor': min(lista),
        'média': sum(lista) / len(lista)
    }
    if sit:
        if resp['média'] >= 6:
            resp['Situação'] = 'Boa'
        elif resp['média'] < 6 and resp['média'] >=4:
            resp['Situação'] = 'Ruim'
        else:
            resp['Situação'] = 'Péssima'
    return resp

aluno = nota(5, 2, 3, 1,sit=True)
print(aluno)
