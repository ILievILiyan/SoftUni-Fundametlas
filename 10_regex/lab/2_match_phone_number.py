import re

text = input()
search_pattern = r'(\+359)([ -])+(2)+\2+(\d{3})+\2+(\d{4}\b)'

result = re.findall(search_pattern, text)
numbers = []

for number in result:
    numbers.append(f"{number[0]}{number[1]}{number[2]}{number[1]}{number[3]}{number[1]}{number[4]}")

print(", ".join(numbers))