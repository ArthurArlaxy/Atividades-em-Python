import moeda

valor = float(input('Digite o Preço: R$'))
por = int(input('Deseja ver o valor aumentado em quantos porcento: %'))
porc = int(input('Deseja ver o valor diminuido em quantos porcento: %'))
print('~'*50)
moeda.dobro(valor)
moeda.metade(valor)
moeda.aumentar(valor,por)
moeda.diminuir(valor,porc)