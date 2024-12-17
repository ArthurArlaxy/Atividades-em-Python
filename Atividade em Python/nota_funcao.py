def nota(*num,sit=False):
    """
    função nota:
    Cria um dicionário com o total de avaliações, mostra a maior e menor nota,média e situação do aluno.
    :param num: recebe a quantidade de avaliações
    :param Sit: se True mostra a situação do aluno
    """
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
