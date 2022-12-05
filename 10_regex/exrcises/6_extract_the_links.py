import re

search_pattern = r'w{3}.([a-zA-Z0-9])+(\-[a-zA-Z0-9]+)*(\.[a-z]+)+\b'

while True:
    text = input()
    if text == "":
        break

    match = re.search(search_pattern, text)
    if match:
        print(match[0])

