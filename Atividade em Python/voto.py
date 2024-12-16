def voto(ano_de_nascimento):
    from datetime import datetime
    idade = datetime.now().year - ano_de_nascimento 
    print(f'Com {idade} anos: ',end='')
    if idade >= 18 and idade < 65:
        print('Voto Obrigatório!!!')
    elif idade < 16:
        print('Não pode Votar!!')
    else:
        print('Voto Opcional!!')
        

nasc = int(input('Digite a data de nascimeto: '))
voto(nasc)
