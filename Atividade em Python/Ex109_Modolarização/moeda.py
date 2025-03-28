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

