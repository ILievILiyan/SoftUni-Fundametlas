import re

text = input()

search_pattern = r'\s(([a-z0-9]+[a-z0-9\.\_\-]*)@[a-z\-]+(\.[a-z]+)+)\b'

result = re.findall(search_pattern, text)
for email in result:
    print(email[0])