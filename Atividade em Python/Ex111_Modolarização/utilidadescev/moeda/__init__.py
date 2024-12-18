def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')

def aumentar(valor, aumento,real=True):
    res = float (valor) + ((valor*aumento)/100)
    if real:
        return moeda(res)
    else:
        return res

def diminuir(valor, diminuição,real=True):
    res = float(valor) - ((valor*diminuição)/100)
    if real:
        return moeda(res)
    else:
        return res

def dobro(valor,real=True):
    res = valor * 2
    if real:
        return moeda(res)
    else:
        return res

def metade(valor,real=True):
    res = valor/2
    if real:
        return moeda(res)
    else:
        return res

def resumo(valor,aumento,diminuição):
    t = 'RESUMO DO VALOR'
    print('-'*40)
    print(f'{t:^40}')
    print('-'*40)
    print(f'Preço analizado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor)}')
    print(f'Metade do preço:  \t{metade(valor)}')
    print(f'{aumento}% de Aumento: \t{aumentar(valor,aumento)}')
    print(f'{diminuição}% de Diminuição:  \t{diminuir(valor,diminuição)}')
    print('-'*40)
