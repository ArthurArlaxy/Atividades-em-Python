def aumentar(valor, aumento):
    valoraum = float (valor) + ((valor*aumento)/100)
    print(f'Aumentando {aumento}%, temos R${valoraum:.2f}')

def diminuir(valor, diminuição):
    valordim = float(valor) - ((valor*diminuição)/100)
    print(f'Diminuido {diminuição}%, temos R${valordim:.2f}')

def dobro(valor):
    dobro = valor * 2
    print(f'O dobro de R${valor:.2f} é R${dobro:.2f}')

def metade(valor):
    metade = valor/2
    print(f'A metade de R${valor:.2f} é R${metade:.2f}')

