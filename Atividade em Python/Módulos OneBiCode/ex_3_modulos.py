import re

def check_character():
    rule = '[A-Za-z0-9]$'
    string = input('Digite uma frase para testar se possui caracteres especiais: ')
    if re.search(rule,string):
        return print(f'Corresponde: {string}')
    else:
        return print(f'Não corresponde: {string}, esse possui caracteres especiais')

def check_character2():
    string=input('Digite uma frase para testar se possui caracteres especiais: ')
    rule = re.compile(r'[^a-zA-Z0-9]')
    string = rule.search(string)
    return  print(not bool(string))

check_character()
check_character2()