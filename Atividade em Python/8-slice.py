gameName = "Fifa 25"
"""
string[início:fim] - índice começa na posição 0 | Índice final -1
passo - determina o incremento. por padrão este número é o 1 
"""

#Toda string a partir da primeira posição
print(gameName[0:])

#Toda a string até a última posição
print(gameName [:7])

#Toda string a partir da terceira posicão
print(gameName[2:])

#toda a string de 2 em 2 caracteres
print(gameName[::2])

#toda a string nos índices ímpares
print(gameName[1::2])

#Inversão de string
print(gameName[::-1])