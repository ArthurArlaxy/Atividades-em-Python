num =[]
for pos in range(0,5):
    num.append(int(input("Digite os valores: ")))
print(f"{num}")

countmax=list()
countmin=list()


for c,n in enumerate(num):
    if n == max(num):
        countmax.append(c)
    elif n == min(num):
        countmin.append(c)
print(f"O maior número foi {max(num)} nas posições {countmax}")
print(f"O maior número foi {min(num)} nas posições {countmin}")

