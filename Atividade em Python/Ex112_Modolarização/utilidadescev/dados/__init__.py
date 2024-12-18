def leiadin():
    while True:
        dinheiro = str(input('Digite o preço: R$')).strip().replace(',','.')
        try:
            dinheiro = float(dinheiro)
            break
        except:
            print(f'\033[31mERRO! "{dinheiro}" é um preço invalido\033[m')
    return dinheiro
