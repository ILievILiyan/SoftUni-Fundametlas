targets = input().split(" ")
targets_list = [int(targets[i]) for i in range(len(targets))]
# target_list = list(map(int, targets))
input_command = input()
while input_command != "End":
    command = input_command.split(" ")
    operation = command[0]
    index = int(command[1])
    value = int(command[2])

    if operation == "Shoot":
        if 0 <= index < len(targets_list):
            targets_list[index] -= value
            if targets_list[index] <= 0:
                targets_list.pop(index)
    elif operation == "Add":
        if 0 <= index < len(targets_list):
            targets_list.insert(index, value)
        else:
            print("Invalid placement!")
    elif operation == "Strike":
        if index - value >= 0 and index + value < len(targets_list):
            del targets_list[(index - value):(index + value + 1)]
        else:
            print('Strike missed!')

    input_command = input()
x = "|".join(map(str, targets_list))
print(x)
