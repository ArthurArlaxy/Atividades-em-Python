def leiadin():
    while True:
        dinheiro = str(input('Digite o preço: R$')).strip().replace(',','.')
        try:
            dinheiro = float(dinheiro)
            break
        except:
            print(f'\033[31mERRO! "{dinheiro}" é um preço invalido\033[m')
    return dinheiro

def leiaint():
    while True:
        r = str(input('Digite um inteiro: '))
        try:    
            int(r)
            break
        except:
            print(f'\033[31mErro! {r} não é um inteiro valido\033[m')
    return r

def leiafloat():
    while True:
        f = str(input('Digite um número real: '))
        try:
            float(f)
            break
        except:
            print(f'\033[31mErro! {f} não é um inteiro valido\033[m')
    return f