listNum = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]



def pesquisa_binaria(lista_ordenada, valor):
    final = len(lista_ordenada) - 1
    inicio = 0
    while inicio <= final:
        meio = int((final + inicio) / 2)
        tentativa = lista_ordenada[meio]
        if tentativa == valor:
            return tentativa
        elif tentativa < valor:
            inicio = meio + 1
        else:
            final = meio - 1
    return None

print(pesquisa_binaria(listNum, 11))