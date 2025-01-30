name = input('Digite o seu nome: ')
"""
- Arquivos 
1 - opção w - write
2 - opção a - append
3 - opção r - read
"""
# Alternativa 1
#file = open('names.txt', 'a')
#file.write(f'{name}\n')
#file.close()

#alternativa 2
with open('dados/names.txt', 'a', encoding='utf-8') as file:
    file.write(f'{name}\n')

