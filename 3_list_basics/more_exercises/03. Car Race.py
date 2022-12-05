input_data = (input()).split(' ')
time_list = [int(input_data[i]) for i in range(len(input_data))]


def time_calculation(x, y, z):
    time_car = 0
    for i in range(x, y, z):
        if time_list[i] != 0:
            time_car += time_list[i]
        else:
            time_car *= 0.8
    return time_car


result_left = time_calculation(0, int(len(time_list) / 2), 1)
result_right = time_calculation(int(len(time_list)) - 1, int(len(time_list) / 2), -1)

if result_left > result_right:
    winner = 'right'
    total_time = result_right
else:
    winner = 'left'
    total_time = result_left
print(f"The winner is {winner} with total time: {total_time:.1f}")
