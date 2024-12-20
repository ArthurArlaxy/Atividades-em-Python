class Pessoa:
    def __init__(self, nome='', cpf=0, numero=0, email='', cartao=None):
        if cartao is None:
            cartao = []
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.email = email
        self.cartao = cartao

    def pegar_dados(self):
        self.nome = str(input('Digite seu nome: '))
        self.cpf = int(input('Digite o CPF: '))
        self.numero = int(input('Digite seu número: '))
        self.email = str(input('Digite seu principal email: '))
        self.cartao = [
            str(input('Digite o nome do banco: ')),
            int(input('Digite o número do cartão: ')),
            int(input('Digite a agência: '))
        ]

    def __str__(self):
        print('-'*50)
        return (f'Nome: {self.nome}\nCPF: {self.cpf}\nNúmero: {self.numero}\n'
                f'Email: {self.email}\nCartão: {self.cartao}')


# Cria uma instância da classe Pessoa e preenche os dados
pessoa1 = Pessoa()
pessoa1.pegar_dados()

# Imprime os dados da instância pessoa1
print(pessoa1)

