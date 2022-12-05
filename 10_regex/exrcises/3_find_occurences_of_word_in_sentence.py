import re

text = input()
search_pattern = input()

regex = fr'\b{search_pattern}\b'

result = re.findall(regex, text, re.IGNORECASE)

print(len(result))