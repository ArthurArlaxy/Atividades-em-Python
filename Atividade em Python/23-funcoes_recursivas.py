def factorial(num):
    if num == 1:
        return 1
    else:
        return (num * factorial(num - 1))

number = int(input('Digite um número para o fatorial: '))
print(f'O fatorial de {number} é igual a {factorial(number)}')

def total_sum(num):
    if num == 1:
        return 1
    else:
        return (num + sum(num - 1))

number = int(input('Digite um número para o fatorial: '))
print(f'O fatorial de {number} é igual a {total_sum(number)}')