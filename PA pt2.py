print('                  GERADOR DE PA')
print(50*'-')
pt= int(input('Primeiro termo: '))
rz= int(input('Razão da PA: '))
c=0
while c != 10:
    c = c + 1
    print(pt, ' -> 'if c < 10 else '', end="")
    pt = pt + rz
print ('\nacabou')