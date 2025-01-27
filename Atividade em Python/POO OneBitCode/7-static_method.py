"""
1 - O metodo de estático não utiliza o parametro referente a classe
2 - O metodo de estático pode acessar, mas não pode modificar o estado da classe 
3 - Usamos o decorator @staticmethod para criar o método estátivo
"""
class Course:
    def __init__(self,name,trail):
        self.name = name
        self.trail = trail

    @staticmethod
    def courses_trails(trail):
        if trail == 'Python Fundamentos':
            courses = ['Dominando python','Módulos e Pip']
        elif trail == 'Automação com o Python':
            courses = ['Automação de tarefas', 'web Scraping']
        else:
            courses = ['A definir']
        return courses

fund = Course('Fundamentos', 'Python Fundamentos')
print(fund.courses_trails('Python Fundamentos'))
print(Course.courses_trails('Automação com o Python'))
print(Course.courses_trails('aibd'))