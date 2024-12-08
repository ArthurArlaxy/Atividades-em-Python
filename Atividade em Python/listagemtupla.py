listagem = ('Cadernos', 50.0, 'notebook',3800.00,'lápis',1.50,'borracha',2.0,'mochila',1.30)

#Tuplas com Formatações como (:^50 'centralização',:.<30 'Formata a esquerda e pôe pontos,:>5.2f formata a direita e põe pontos flutuantes')
print(50*'-')
print(f"{'Listagem de Compras':^50}")
print(50*'-')


for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end='')
    else:
        print(f'R${listagem[pos]:>5.2f}')
print(50*'-')
