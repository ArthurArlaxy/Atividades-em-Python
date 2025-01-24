class Movie:
    def __init__(self, name , yearLaunch, includePlan, note, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includePlan
        self.note =  note
        self.durationMinutes = durationMinutes
    
    def __str__(self):
        return f'Filme: {self.name}\nAno de lançamento: {self.yearLaunch}\nIncluso: {self.includedPlan}\n'

mario = Movie("Super Mario Bros", 2023, True, 8.0, 124)
homemAranha = Movie("Homem Aranha", 2019, True, 10.0, 144)
print(mario)
print(homemAranha)
