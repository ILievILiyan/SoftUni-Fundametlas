input_data = (input()).split(', ')
list_with_numbers = [int(input_data[i]) for i in range(len(input_data))]
count_of_beggars = int(input())

new_list_for_printing = []
start = 0

for _ in range(count_of_beggars):
    current_count = 0
    for i in range(start, len(list_with_numbers), count_of_beggars):
        current_count += list_with_numbers[i]
    new_list_for_printing.append(current_count)
    start += 1

print(new_list_for_printing)
