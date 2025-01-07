class Aluno():
    def __init__(self):
        self.nome  =''
        self.idade = 0
        self.turma = ''
    
    def pegar_info(self):
        self.nome = str(input('NOME:'))
        while True:
            try:
                self.idade = int(input('IDADE:'))
                if self.idade < 0:
                    raise print('Não existe idade negativa.', end='')
                break
            except:
                print('Tipo invalido, ',end='')
        self.turma = str(input('Turma: '))

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
        if id in self.base:
            while True:
                confirmacao = input(f"Você tem certeza que deseja remover o aluno com ID {id}? (s/n): ").strip().lower()[0]
                if confirmacao in 'sn':
                    if confirmacao in 's':
                        del self.base[id]
                        print(f"Aluno com ID {id} removido.")
                        break
                    else:
                        print("Operação cancelada.")
                        break
                else:
                    print('Resposta invalida. ',end='')
        else:
            print("ID inválido.")
    
    def update(self):
        id= int(input('Que aluno você deseja atualizar com o ID: '))
        if id in self.base:
            aluno = self.base[id]
            nome = str(input(f'Nome: {aluno.nome}, Novo nome:')).strip()
            if nome:
                aluno.nome = nome
            idade = str(input(f'Idade: {aluno.idade}, Novo idade:')).strip()
            if idade:
                aluno.idade = idade
            turma = str(input(f'turma: {aluno.turma}, Novo Turma:')).strip()
            if turma:
                aluno.turma = turma
        else:
            print('Aluno não encontrado')



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
