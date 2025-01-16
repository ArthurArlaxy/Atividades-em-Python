import pprint

gamesDict = {
    'Fifa 23' : {
        'yearLaunch': 2022,
        'classification': 8.5,
        'genre': ['esporte','familia']
    },
    'Fortnite': {
        'yearLaunch': 2020,
        'classification': 10,
        'genre': ['aventura','familia','battle royale']
    },
    'Mario': {
        'yearLaunch': 1996,
        'classification': 8.5,
        'genre': ['2d','aventura']
    }
}

pp = pprint.PrettyPrinter(depth=3)
pp.pprint(gamesDict)

print(gamesDict['Mario']['genre'])

gamesDict['Fortnite']['Foda'] = True

print(gamesDict['Fortnite'])

del gamesDict['Mario']
pp.pprint(gamesDict)

for jogos in gamesDict.items():
    print(jogos)