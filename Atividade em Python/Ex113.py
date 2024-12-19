def leiaint():
    while True:
        try:    
            r = str(input('Digite um inteiro: ')).strip()
            r = int(r)
            break
        except KeyboardInterrupt:
            print(f'\n\033[31mO usuário não digitou\033[m')
            r= 'nenhum'
            return 'nenhum'
        except:
            print(f'\033[31mErro! "{r}" não é um inteiro valido\033[m')
    return r

def leiafloat():
    while True:
        try:
            f = str(input('Digite um número real: ')).strip()
            f = float(f)
            break
        except KeyboardInterrupt:
            print('\n\033[31mO usuário não digitou\033[m')
            return 'nenhum'
        except :
            print(f'\033[31mErro! "{f}" não é um real valido\033[m')
    return f


inteiro = leiaint()
real = leiafloat()
print('~'*100)
print(f'O número inteiro digitado foi {inteiro} e o real foi {real}')