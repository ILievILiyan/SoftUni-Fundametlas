def tribinacci_sequence(num):
    new_list = [1]
    for i in range(1, num):
        if len(new_list) < 3:
            current_num = sum(new_list)
            new_list.append(current_num)
        else:
            current_num = sum(new_list[i-3:])
            new_list.append(current_num)
    return new_list


number = int(input())
result = tribinacci_sequence(number)
print(' '.join(map(str, result)))
