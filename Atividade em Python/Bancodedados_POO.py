class BancoDeDados():
    def __init__(self):
        self.base = {}
    
    def adicionar(self,nome, lista = []):
        if 'Cliente' not in self.base:
            self.base['Cliente'] = {nome:lista}
        else:
            self.base['Cliente'].update({nome:lista})
    
    def listar(self):
        if 'Cliente' in self.base:
            for nome, dados in self.base['Cliente'].items():
                print(f'{nome} {dados}')
    
    def delete(self,nome):
        if nome in self.base['Cliente']:
            del self.base['Cliente'][nome]


clientes = BancoDeDados()

clientes.adicionar('Arthur',[976739777 , 'Rua dr luiz Palmier 1001'])
clientes.adicionar('Maria Luiza', [123456789, "Rodrigo's lanches"])
clientes.adicionar('Elisa', [987654321, 'Rua Dr Luiz palmier 1001'])

clientes.listar()

clientes.delete('Arthur')

clientes.listar()
