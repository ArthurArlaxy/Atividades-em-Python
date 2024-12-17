def nota(num =[],sit=False):
    """
    função nota:
    Cria um dicionário com o total de avaliações, mostra a maior e menor nota,média e situação do aluno.
    :param num: recebe a quantidade de avaliações
    :param Sit: se True mostra a situação do aluno
    """

    resp = {
        'Total': len(num),
        'Maior': max(num),
        'Menor': min(num),
        'média': sum(num) / len(num)
    }
    if sit:
        if resp['média'] >= 6:
            resp['Situação'] = 'Boa'
        elif resp['média'] < 6 and resp['média'] >=4:
            resp['Situação'] = 'Ruim'
        else:
            resp['Situação'] = 'Péssima'
    return resp


num=[]
while True:
    quan = str(input('Digite a quantidade de avaliações: '))
    if quan.isnumeric():
        quan =int(quan)
        break
    else:
        print('Tente Novamente. ',end='')

for c in range(0,quan):
    while True:
        n = str(input(f'Digite a {c+1}° nota: '))
        if n.isnumeric():
            n =int(n)
            num.append(n)
            break
        else:
            print('Tente Novamente. ',end='')
aluno = nota(num)
print(aluno)
