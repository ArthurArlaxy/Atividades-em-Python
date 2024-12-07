sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dado inválido, Digite seu sexo novamente:')).strip().upper()[0]
print('O sexo {} foi definido '.format(sexo))