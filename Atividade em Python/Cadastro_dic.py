from datetime import datetime

print('FAÇA SEU CADASTRO')
cad = {
    'nome': str(input('Nome: ')),
    'idade':  datetime.now().year - int(input('Ano de nascimento: ')), 
    'CLT': int(input('Digite o número da carteira de trabalho (0 caso não possua): '))}

if cad['CLT'] != 0:
    cad['contratação'] = int(input('Ano de Contratação: '))
    cad['salário'] = float(input('Salário: R$'))

print('-='*25)
print(f'O nome é {cad["nome"]}')
print(f'A idade é {cad["idade"]}')
print(f'A CTPS é {cad["CLT"]}')
if cad["CLT"] != 0:
    print(f'O ano de contratação foi em {cad["contratação"]}')
    print(f'O salário é R${cad["salário"]} ')
    print(f'Poderá se aposentar em {cad["contratação"]+35} com {cad["idade"] + cad["contratação"] - datetime.now().year + 35} ')