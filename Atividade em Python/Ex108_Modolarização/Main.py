import moeda

valor = float(input('Digite o Preço: R$'))
por = int(input('Deseja ver o valor aumentado em quantos porcento: %'))
porc = int(input('Deseja ver o valor diminuido em quantos porcento: %'))
print('~'*50)
print(f'O dobro de {moeda.moeda(valor)} é {moeda.moeda(moeda.dobro(valor))}')
print(f'A metade de {moeda.moeda(valor)} é {moeda.moeda(moeda.metade(valor))}')
print(f'Aumentando {por}%, temos {moeda.moeda(moeda.aumentar(valor,por))}')
print(f'Diminuindo {porc}%, temos {moeda.moeda(moeda.diminuir(valor,porc))}')