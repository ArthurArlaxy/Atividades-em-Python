name = input('Digite o nome: ')
yearLaunch = int(input('Digite o ano: '))
gamePrice = float(input('Digite o preço\n'))
planIncluded = (input('Digite se está incluso: '))


#Alternativa 1
print("----- Dados do jogo -----")
print('Nome do jogo: ',name)
print('Ano do jogo: ',yearLaunch)
print('Preço do jogo: ',gamePrice)
print('Está incluso no plano: ',planIncluded)

#Alternativa 2 
print("----- Dados do jogo -----")
print('Nome do jogo: ',name,'\nAno do jogo: ',yearLaunch,'\nPreço do jogo: ',gamePrice,'\nEstá incluso no plano: ',planIncluded)

#Alternativa 3
print("----- Dados do jogo -----")
print(f'Nome do jogo: {name}\nAno do jogo: {yearLaunch}\nPreço do jogo: {gamePrice}\nEstá incluso no plano: {planIncluded}')