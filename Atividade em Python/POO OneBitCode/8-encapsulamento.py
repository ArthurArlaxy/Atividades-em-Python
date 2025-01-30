class Employee:
    def __init__(self, name, salary):
        self.__name = name
        self.__salary = salary
    
    def __str__(self):
        return f'Nome: {self.__name} | Salario: {self.__salary}'

arthur = Employee('Arthur', 10000)
fulano = Employee('Fulano', 11000)

print(arthur)
print(fulano)
fulano.__salary = 23123023
print(fulano)
