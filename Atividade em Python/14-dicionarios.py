gameFifa = {
    "name": 'Fifa 23',
    'yearLaunch':'2022',
    'gamePrice': 90.50,
    'genre': ['esporte, família']
}

print(gameFifa)
print(len(gameFifa))
print(type(gameFifa))

print(gameFifa['genre'])
print(gameFifa.get('gamePrice'))

print(gameFifa.keys())

print(gameFifa.values())

print(gameFifa.items())

gameFifa['players'] = 2
print(gameFifa)

gameFifa['players'] = 3
print(gameFifa)

gameFifa.update({'players': 1})
print(gameFifa)

gameFifa.pop('players')
print(gameFifa)