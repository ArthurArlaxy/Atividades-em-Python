name = input('Digite o nome(Deve conter pelo menos duas palavras separadas por espaço): ').lower()
gameDescription = """
Fifa é um jogo de Futebol, desenvolvido pela EA Sports,
jogo Mercenário, possibilita jogar localmente ou online
"""

print(name[0]+name[1:].replace(name[0],'$'))

sep = name.split(' ')
troca1 = sep[0][:2]
troca2 = sep[1][:2]
print(sep[0].replace(troca1,troca2),sep[1].replace(troca2,troca1))
