num =[]
for pos in range(0,5):
    num.append(int(input(f"Digite um valor para posição {pos}: ")))
print(f"Os números presentes são {num}")

countmax=list()
countmin=list()

for c,n in enumerate(num):
    if n == max(num):
        countmax.append(c)
    elif n == min(num):
        countmin.append(c)

if max(num) != min(num):
    print(f"O maior número foi {max(num)} nas posições ",end='')
    for l in countmax:
        print(f"{l}",end="... ")
    print(f"\nO menor número foi {min(num)} nas posições ",end="")
    for m in countmin:
        print(f"{m}",end='... ')
else:
    print(f"O maior e menor número foi {n} e ele estava em todas as posiçôes : ",end="")
    for i in countmax:
        print(f'{i}',end='... ')