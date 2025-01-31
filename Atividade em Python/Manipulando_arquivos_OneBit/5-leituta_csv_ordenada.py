courses = []

with open('dados/courses.csv', 'r', encoding='utf-8') as file:
    for line in file:
        language, categorty = line.rstrip().split(',')
        courses.append(f'{language} -{categorty}')

courses.sort()
for course in courses:
    print(course)