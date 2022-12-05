import re

pattern = r'(#|\|)([a-zA-Z ]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1'

text = input()
result = re.findall(pattern, text)
calories = sum(int(foods[3]) for foods in result)
days_to_eat = int(calories/2000)

print(f"You have food to last you for: {days_to_eat} days!")

for food in result:
    print(f"Item: {food[1]}, Best before: {''.join([food[2]])}, Nutrition: {food[3]}")