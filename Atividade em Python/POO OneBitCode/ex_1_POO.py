class Movie:
    def __init__(self, name , yearLaunch, includePlan, durationMinutes):
        self.name = name
        self.yearLaunch = yearLaunch
        self.includedPlan = includePlan
        self.note = 0
        self.durationMinutes = durationMinutes
        self.totalEvaluators = 0
        self.totalNote = 0
    
    def __str__(self):
        return f'Filme: {self.name}\nAno de lançamento: {self.yearLaunch}\nIncluso: {self.includedPlan}\n'

    def techinal_sheet(self):
        print('-=-= Dados do Filme =-=-')
        print(f'Filme: {self.name}')
        print(f'Ano do lançamento: {self.yearLaunch}')
        print(f'Includo: {self.includedPlan}')
        print(f'Note: {self.note}')
        print(f'Duração do Filme: {self.durationMinutes}')
        print(f'Total de Avaliadores: {self.totalAvaliation}\n')
    
    def avaliationNote(self):
        note = float(input(f'Digite sua nota para o filme {self.name}: '))
        self.totalEvaluators += 1 
        self.totalNote += note
        self.note = self.totalNote / self.totalEvaluators 


mario = Movie("Super Mario Bros", 2023, True, 124)
homemAranha = Movie("Homem Aranha", 2019, True, 144)
homemAranha.techinal_sheet()

homemAranha.avaliationNote()
homemAranha.techinal_sheet()
homemAranha.avaliationNote()
homemAranha.techinal_sheet()
homemAranha.avaliationNote()
homemAranha.techinal_sheet()
homemAranha.avaliationNote()
homemAranha.techinal_sheet()