con = 0
termo = int(input('Digite quanto termos deseja saber: '))
opção= ''
f = 0 
t1 = 0
t2 = 1 
t3 = 0
print('{} -> {} -> '.format(t1,t2),end='')
while con != termo:
        con = con + 1
        t3 = t1 + t2
        print(t3,'-> ', end='')
        t1= t2
        t2= t3
print('Fim')
