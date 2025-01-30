"""
1 - O metodo de classe utiliza o parametro referente a classe
2 - O metodo de classe pode acessar ou modificar o estado da classe 
3 - Usamos o decorator @classmethod para criar o método classe 
"""

class Console:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    @classmethod
    def from_text(cls, string):
        import re
        item = re.findall("é \w*", string)
        name = item[0][2:]
        price = item[1][2:]
        return cls(name, int(price))
    
    @classmethod
    def dados(cls):
        name = input('Digite o nome do seu console: ')
        price = int(input('Digite o preço do console: '))
        return cls(name, price)
    
    def __str__(self):
        return f'Nome : {self.name} | Price: {self.price}'
    
wiiU = Console.from_text("Meu video game é WiiU e o preço é 1000 reais")
xboxSeries = Console.dados()
print(wiiU)
print(xboxSeries.__dict__)
