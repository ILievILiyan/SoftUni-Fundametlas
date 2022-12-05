input_distance = input().split(" ")
distances = list(map(int, input_distance))
total_sum = 0

while len(distances) != 0:
    index = int(input())
    current_num = 0
    if 0 <= index < len(distances):
        current_num = distances.pop(index)
    elif index < 0:
        current_num = distances[0]
        distances[0] = distances[-1]
    else:
        current_num = distances[-1]
        distances[-1] = distances[0]
    total_sum += current_num

    for nums in range(len(distances)):
        if distances[nums] > current_num:
            distances[nums] -= current_num
        else:
            distances[nums] += current_num
print(total_sum)
