
array_input = input().split(" ")
array_list = [int(array_input[i]) for i in range(len(array_input))]
# array_list = list(map(int, array_input))

command = input()
while command != "end":
    command_list = command.split(" ")
    operation = command_list[0]

    if operation == "swap" or operation == "multiply":
        i_1 = int(command_list[1])
        i_2 = int(command_list[2])
        if operation == "swap":
            array_list[i_1], array_list[i_2] = array_list[i_2], array_list[i_1]
        elif operation == "multiply":
            array_list[i_1] *= array_list[i_2]
    elif operation == "decrease":
        for i in range(len(array_list)):
            array_list[i] -= 1
        # array_list = list(map(lambda x: x -1, array_list))
    command = input()

print(", ".join(map(str, array_list)))