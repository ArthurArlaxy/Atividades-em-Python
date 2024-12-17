from time import sleep

def fatorial(num=1,show=False):
    """
    Mostra um fatorial de número através de um loop com multiplicação
    num = Receber um número
    
    for c in range(num,0,-1)

        if show :                  \
            if c == 1:              \
                print(c,end=' = ')    > Se show = True --- mostra o cálculo
            else:                   /
                print(c,end=' x ') /

        f*=c  --- é responsavel por fazer o fatorial
    return f  --- Passa o valor para o programa principal
    """
    f = 1
    for c in range(num,0,-1):
        if show :
            if c == 1:
                print(c,end=' = ')
            else:
                print(c,end=' x ')
        f*=c
    return f

def infos(num=[]):
    print('-='*25)
    sleep(0.5)
    print(f'Analizando os valores {num}')
    sleep(0.5)
    print(f'Foram informados {len(num)} valores ao todo')
    sleep(0.5)
    print(f'O maior valor foi {max(num)} e o menor foi {min(num)} e a soma de todos eles foi {sum(num)}')
    print('-='*25)

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