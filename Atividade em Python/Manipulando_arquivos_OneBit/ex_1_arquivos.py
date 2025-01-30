leituraTotal = []

def Leitura_de_arquivos(arquivo, linhas):
    from itertools import islice
    with open(f'dados/{arquivo}','r',encoding='utf-8') as file:
        for line in islice(file, linhas):
            print(line.rstrip())

Leitura_de_arquivos('texto.txt', 2)