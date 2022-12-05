input_data = (input()).split(', ')
digits_list = [int(input_data[i]) for i in range(len(input_data))]
count_zeros = 0

while 0 in digits_list:
    digits_list.remove(0)
    count_zeros += 1

for deleted_zeroes in range(count_zeros):
    digits_list.append(0)

print(digits_list)