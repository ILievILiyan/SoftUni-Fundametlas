import re

text = input()
search_pattern = r'(\d{2})([\/.-])([A-Z][a-z]{2})\2(\d{4})'

result = re.findall(search_pattern, text)
dates = []

for date in result:
    print(f"Day: {date[0]}, Month: {date[2]}, Year: {date[3]}")
