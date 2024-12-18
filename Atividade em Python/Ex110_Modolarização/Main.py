import moeda

valor = float(input('Digite o Preço: R$'))
por = int(input('Deseja ver o valor aumentado em quantos porcento: %'))
porc = int(input('Deseja ver o valor diminuido em quantos porcento: %'))
moeda.resumo(valor, por, porc)