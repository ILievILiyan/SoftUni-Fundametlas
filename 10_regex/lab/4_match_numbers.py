import re

sequence = input()

expression = r"(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.[0-9]+)?($|(?=\s))"

# find = re.finditer(expression, sequence)  # if you would like to print it by the group name
find = re.finditer(expression, sequence)  # if you would like to print it with indexes of the group

for i in find:
    print(i.group(), end=' ')
    # print(f'Day: {i.group("day")}, Month: {i.group("month")}, Year: {i.group("year")}')