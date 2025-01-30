"""
- Arquivos 
1 - opção w - write
2 - opção a - append
3 - opção r - read
"""
with open('dados/names.txt', 'r', encoding= 'utf-8') as file:
    for line in file:
        print(f'{line.rstrip()}')