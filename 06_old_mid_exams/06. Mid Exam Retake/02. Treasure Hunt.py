initial_loot = input().split("|")
count_of_symbols = 0
hunt_failed = False

while True:
    command_split = input().split(" ")

    if command_split[0] == "Yohoho!":
        break
    current_command = command_split[0]

    if current_command == "Loot":
        inserting_items = [initial_loot.insert(0, item)
                           for item in command_split[1:len(command_split)] if item not in initial_loot]

    elif current_command == "Drop":
        index = int(command_split[1])
        if 0 <= index <= len(initial_loot):
            x = initial_loot.pop(index)
            initial_loot.append(x)

    elif current_command == "Steal":
        count_stolen_items = int(command_split[1])
        if count_stolen_items < len(initial_loot):
            stolen_items = initial_loot[-count_stolen_items:]
            for item in stolen_items:
                if item in initial_loot:
                    initial_loot.remove(item)
        else:
            stolen_items = initial_loot.copy()
            initial_loot.clear()
            hunt_failed = True
        print(", ".join(stolen_items))

if not hunt_failed:
    count_of_symbols_list = [len(items) for items in initial_loot]
    count_of_symbols = sum(count_of_symbols_list) / len(count_of_symbols_list)
    print(f'Average treasure gain: {count_of_symbols:.2f} pirate credits.')
else:
    print("Failed treasure hunt.")
