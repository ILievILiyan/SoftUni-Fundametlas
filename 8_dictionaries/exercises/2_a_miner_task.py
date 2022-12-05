items_list = []
command = input()
items_dictionary = {}

while command != "stop":
    items_list.append(command)
    command = input()

for item in range(0, len(items_list), 2):
    key = items_list[item]
    value = int(items_list[item + 1])
    if key not in items_dictionary.keys():
        items_dictionary[key] = 0
    items_dictionary[key] += value

for key, value in items_dictionary.items():
    print(f"{key} -> {value}")
