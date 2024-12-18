def aumentar(valor, aumento):
    res = float (valor) + ((valor*aumento)/100)
    return res

def diminuir(valor, diminuição):
    res = float(valor) - ((valor*diminuição)/100)
    return res

def dobro(valor):
    res = valor * 2
    return res

def metade(valor):
    res = valor/2
    return res

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:.2f}'.replace('.',',')
