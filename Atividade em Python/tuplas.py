#TUPLAS SÃO IMUTÁVEIS

#Isso é uma tupla
lanche=('Hamburguer','Suco','Ketchup', 'Pudim')

#forma de repetir a tupla separadamente
for comida in lanche:
    print(f'Eu vou comer {comida}')
print("Vai ser lindo")

#expressão lenght (significa comprimento)
print(len(lanche))

#Outra forma de repetir a comida de 1 a 1 possível realizar contagem
for cont in range(0, len(lanche)):
    print(f'vou comer {lanche[cont]}')
print('Vai ser lindo!!!')

#Outra forma de repetir a comida de 1 a 1 possível realizar contagem
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} e ela se encontra na posição {pos}')

#Mostra a tupla em Ordem
print(sorted(lanche))

#Deleta a variavel
del() 

a = (2,3,4)
b = (4,5,6,7)
c = a + b
print(c)
print(c.count(4))
print(c.index(3))