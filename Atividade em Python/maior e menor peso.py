lista_pesos = []
num = 0
for peso in range(0,5,):
    num = num + 1
    n = float(input('Digite o peso da {}° pessoa:'.format(num)))
    lista_pesos.append(n)
print(lista_pesos)
print('O peso maximo encontrado foi {}\nE o peso mínimo foi {}'.format(max(lista_pesos),min(lista_pesos)))
