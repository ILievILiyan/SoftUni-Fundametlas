import re

text = input()
pattern = r'(?P<surr>\#|\|)(?P<product>[A-Za-z ]+)\1(?P<date>\d{2}/\d{2}/\d{2})\1(?P<calories>\d+)'

result = re.finditer(pattern, text)

total_calories = 0
foods_to_print = []
for match in result:
    data = match.groupdict()
    foods_to_print.append(f'Item: {data["product"]}, Best before: {data["date"]}, Nutrition: {data["calories"]}')
    total_calories += int(data['calories'])
days = int(total_calories / 2000)
print(f"You have food to last you for: {days} days!")
print("\n".join(foods_to_print))
