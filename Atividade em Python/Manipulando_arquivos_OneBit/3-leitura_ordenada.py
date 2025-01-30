names = []
with open('dados/names.txt', 'r', encoding='utf-8') as file:
    for line in file:
        names.append(line.rstrip())

names.sort()
print(names)
for name in names:
    print(name)