class Movie:
    name = ""
    yearLaunch = 0
    includedPlan = False
    note =  0
    durationMinutes = 0

#primeiro Filme
avatar = Movie()
avatar.name = 'Avatar: A lenda de yang'
avatar.yearLaunch = 2016
avatar.includedPlan = False
avatar.note = 10.0
avatar.durationMinutes = 113

#Segundo Filme

bad = Movie()
bad.name = "Bad Boys"
bad.yearLaunch = 2022
bad.includedPlan = True
bad.note = 8.0
bad.durationMinutes = 130

print('Dados dos filmes'.center(100,'-'))
print(f'Nome do filme: {avatar.name} |  Data de lançamento: {avatar.yearLaunch}'.center(100))
print(f'Nome do filme: {bad.name} |  Data de lançamento: {bad.yearLaunch}'.center(100))