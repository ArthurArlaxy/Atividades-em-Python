class Product:
    def __init__(self,name, price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f'Nome: {self.name}\nPreço: R${self.price:.2f}'

    def descount(self, descount):
        return print(f'O preço inicial é R${self.price:.2f} e com o desconto de {descount}% ficaria R${self.price - (self.price * (descount / 100 )):.2f}')
    
mesa = Product('mesa', 230)
cadeira = Product('cadeira',100)
lapis = Product('lapis', 3.5)

print(mesa)
mesa.descount(23)
cadeira.descount(14)
lapis.descount(50)