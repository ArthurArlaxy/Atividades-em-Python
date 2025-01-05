class Aluno():
    def __init__(self):
        self.nome  =''
        self.idade = 0
        self.turma = ''
    
    def pegar_info(self):
        self.nome = str(input('NOME:'))
        self.idade = int(input('IDADE:'))
        self.turma = str(input('Turma'))

class BancoDeDados():
    def __init__(self):
        self.base = {}
        self.contador = 0

    def adicionar(self, aluno):
        self.contador += 1
        self.base[self.contador] = aluno
    
    def listar(self):
        for id, aluno in self.base.items():
            print(f"ID: {id}, Nome: {aluno.nome}, Idade: {aluno.idade}, Turma: {aluno.turma}")
    
    def deletar(self):
        id = int(input('Que Aluno deseja remover?'))
        del self.base[id]

banco = BancoDeDados()
aluno1 = Aluno()
aluno1.pegar_info()
banco.adicionar(aluno1)
banco.listar()
aluno2 = Aluno()
aluno2.pegar_info()
banco.adicionar(aluno2)
banco.deletar()
banco.listar()
