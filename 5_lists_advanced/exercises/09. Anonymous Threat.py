def merge(start_i, end_i, string):
    if start_i < 0:
        start_i = 0
    if end_i >= len(string):
        end_i = len(string)
    result = "".join(string[start_i:end_i+1])
    del string[start_i:end_i+1]
    if result != "":
        string.insert(start_i, result)
    return string


def divide(index, partitions, string):
    string_to_devide = string.pop(index)
    start = 0

    if partitions > len(string[index]):
        step = 1
    else:
        step = len(string[index]) // partitions

    for current_part in range(partitions):
        if current_part == partitions - 1:
            string.insert(index, string_to_devide[start::])
            break
        else:
            string.insert(index, string_to_devide[start: start + step:])
        start += step
        index += 1
    return string


input_line = input().split(" ")

while True:
    input_commands = input()

    if input_commands == "3:1":
        break

    split_command = input_commands.split(" ")
    if split_command[0] == "merge":
        start = int(split_command[1])
        end = int(split_command[2])
        input_line = merge(start, end, input_line)

    if split_command[0] == "divide":
        index_ = int(split_command[1])
        partitions_ = int(split_command[2])
        input_line = divide(index_, partitions_, input_line)


print(*input_line)

