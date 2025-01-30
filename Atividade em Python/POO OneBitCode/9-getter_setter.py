class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary
    
    def __str__(self):
        return f'Nome: {self.name} | Salario: {self.__salary}'
    
    #Método para buscar dados
    def get_salary(self):
        return self.__salary
    
    #Método para modificar atributo privado
    def set_salary(self,salary):
        self.__salary = salary

arthur = Employee('Arthur', 10000)
fulano = Employee('Fulano', 11000)

print(arthur)
print(fulano)
fulano.__salary = 23123023
print(fulano)
print(arthur.get_salary())
arthur.set_salary(15000)
print(arthur)