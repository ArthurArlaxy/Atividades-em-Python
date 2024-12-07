fem20=0
idadef=[]
idade_lista=[]
nomem = ''
fem = 0
masc = 0
num = 0
maior = 0
for c in range(0,4):
    num = num + 1
    print(5*'-','{}° PESSOA'.format(num),5*'-')
    nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    idade_lista.append(idade)
    sexo = str(input('Sexo[M/F]')).upper()
    if sexo == 'M':
        masc = masc + 1
        if idade > maior:
            maior = idade
            nomem = nome
    elif  sexo == 'F' :
        fem = fem + 1
        idadef.append(idade)
        if idade > 20:
            fem20 = fem20 + 1
    else:
        print('Essa opção não existe')
soma = sum(idade_lista)
media = soma/len(idade_lista)
somaf = sum(idadef)
mediaf = somaf/fem
print('A média da idade do grupo {}'.format(media))
print('O homem mais velho tem {} anos e o nome é {}'.format(maior,nomem))
print('Ao todo são/é {} mulheres e a média de idade é {}'.format(fem,mediaf))
print('O Número de mulheres abaixo de 20 anos é {}'.format(fem20))
