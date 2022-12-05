import re

num_of_lines = int(input())

pattern = r'(\|)([A-Z]{4,})\1:(\#)([a-zA-z]+ [a-zA-Z]+)\3'

for _ in range(num_of_lines):
    current_input = input()

    result = re.search(pattern, current_input)

    if result:
        name = result[2]
        title = result[4]
        print(f'{name}, The {title}')
        print(f'>> Strength: {len(name)}')
        print(f'>> Armor: {len(title)}')
    else:
        print("Access denied!")

