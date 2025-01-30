with open('dados/courses.csv', 'r', encoding='utf-8') as file:
    for line in file:
        language, category = line.rstrip().split(',')
        print(f'{language} -{category}')