import re


text = input()
pattern = r'(\=|\/)([A-Z][a-zA-Z]{2,})\1'

result = re.findall(pattern, text)
destinations = []
points = 0

for current_destination in result:
    destinations.append(current_destination[1])
    points += len(current_destination[1])

print(f'Destinations: {", ".join(destinations)}')
print(f'Travel Points: {points}')


