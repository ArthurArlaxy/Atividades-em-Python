def sum(*num):
    sum_total=0
    for n in num:
        sum_total += n
    print(f'A Soma foi {sum_total}')

sum(20,2,23,81)

def presentation(**materias):
    for k, v in materias.items():
        print(f'{k} - {v}')

presentation(name ='Backend', subject='python, database, API')
