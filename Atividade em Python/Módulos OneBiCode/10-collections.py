from collections import Counter, namedtuple, deque
from operator import itemgetter

# 1 - Conta itens de uma lista
fruits = ["Maçã", "Banana", "Uva", "Pêra", "Uva","Maçã", "Uva", "Banana"]
print(fruits)
print(Counter(fruits))

# 2 - Utilizando uma tupla nomeada
game = namedtuple('game', ['name', 'price', 'note'])
g1 = game("Fifa 23", 90.50, 8.5)
g2 = game("Resident Evil 4", 300.00, 10.0)
print(g1)
print(g2)

# 3 - Ordenando dicionários
studants = {"Pedro":24, "Ana":22, "Ronaldo":26, "Janaina":25}
studants_sort = sorted(studants.items(), key=itemgetter(0))
print(studants)
print(studants_sort)

# 4 - Utilizando fila ambas extremidades
valor = deque([20,40,60,80])
valor.appendleft(10)
print(valor)
valor.append(90)
valor.popleft()
print(valor)