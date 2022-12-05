import re

search_pattern = r'\d+'
numbers = []

while True:
    text = input()
    if text == "":
        break
    result = re.findall(search_pattern, text)
    if result:
        print(*result, end=" ")
