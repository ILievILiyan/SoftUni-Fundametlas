import re

text = input()
search_pattern = r'(?i)(?<=\s|^|\W) (?=\s|$|\W)'

result = re.findall(search_pattern, text, re.IGNORECASE)

print(len(result))
