num = suce = ante = int(input('Digite um número: '))
suce += 1
ante -= 1

print(f'Seu número foi {num}, o antecessor dele é {ante}, e o sucessor é {suce}')

num=0
for c in range(0,4):
    n = float(input(f'Digite o {c+1}° nota: '))
    num += n

media = num / 4
print(f'A média foi {media}')