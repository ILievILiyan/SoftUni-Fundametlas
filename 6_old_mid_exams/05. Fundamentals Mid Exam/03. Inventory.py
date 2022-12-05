words = input().split(", ")

command = input()
while command != "Craft!":
    command_split = command.split(" - ")
    operation = command_split[0]
    item = command_split[1]
    if operation == "Collect":
        if item not in words:
            words.append(item)
    elif operation == "Drop":
        if item in words:
            words.remove(item)
    elif operation == "Combine Items":
        item = item.split(":")
        old_item = item[0]
        new_item = item[1]
        if old_item in words:
            index_old_item = words.index(old_item)
            words.insert(index_old_item + 1, new_item)
    elif operation == "Renew":
        if item in words:
            words.append(item)
            words.remove(item)
    command = input()

print(", ".join(map(str, words)))
