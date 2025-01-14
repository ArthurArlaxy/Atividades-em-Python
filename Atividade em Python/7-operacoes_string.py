gameDescription = """
Fifa é um jogo de Futebol desenvolvido pela EA Sports
Jogo Mercenário que possibilita jogar localmente ou online
"""
line = '='
gameName = "Fifa"
gameVersion = " 25"
#Operação de concatenação
gameFullName = gameName + gameVersion
#Operação de multiplicação
print(line * 20)
print(gameFullName)
print(line * 20)

#Procura de palavra dentro de um texto
print('Fifa'in gameDescription)
print('Handball' in gameDescription)