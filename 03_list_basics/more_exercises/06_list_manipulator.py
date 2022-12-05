input_data = (input()).split(' ')
numbers_list = [int(input_data[i]) for i in range(len(input_data))]
even_list = []
odd_list = []


def max_min_even_odd(max_or_min, even_or_odd):
    if max_or_min == "max":
        max_or_min = max
    elif max_or_min == "min":
        max_or_min = min

    if even_or_odd == "even":
        even_or_odd = even_list
    elif even_or_odd == "odd":
        even_or_odd = odd_list

    if len(even_or_odd) > 0:
        return max_or_min(even_or_odd)
    else:
        return "empty"


def recalculate_even_odd_list():
    even_list.clear()
    odd_list.clear()
    for value in numbers_list:
        if value % 2 == 0:
            even_list.append(value)
        else:
            odd_list.append(value)


recalculate_even_odd_list()

command = input().split(' ')
while command[0] != "end":
    first_command = command[0]
    second_command = command[1]

    if first_command == "exchange":
        if 0 <= int(second_command) < len(numbers_list):
            for index in range(int(second_command) + 1):
                numbers_list.append(numbers_list[0])
                del numbers_list[0]
            recalculate_even_odd_list()
        else:
            print('Invalid index')

    if first_command == "max" or first_command == "min":
        current_value = max_min_even_odd(first_command, second_command)
        if current_value != "empty":
            for i in range(len(numbers_list) - 1, -1, -1):
                if numbers_list[i] == current_value:
                    print(i)
                    break
        else:
            print('No matches')

    if first_command == "first" or first_command == "last":
        second_command = command[2]
        third_command = int(command[1])
        if third_command > len(numbers_list):
            print('Invalid count')
            command = input().split(' ')
            continue
        if second_command == "even":
            if third_command <= len(even_list) and first_command == "first":
                print(even_list[:third_command])
            elif third_command <= len(even_list) and first_command == "last":
                print(even_list[(len(even_list) - third_command)::])
            else:
                print(even_list)
        elif second_command == "odd":
            if third_command <= len(odd_list) and first_command == "first":
                print(odd_list[:third_command])
            elif third_command <= len(odd_list) and first_command == "last":
                print(odd_list[(len(odd_list) - third_command)::])
            else:
                print(odd_list)

    command = input().split(' ')
print(numbers_list)
