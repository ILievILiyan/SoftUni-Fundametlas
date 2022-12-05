numbers = (input()).split(' ')
numbers_list = [int(numbers[i]) for i in range(len(numbers))]
nums_to_delete = int(input())


for numbers in range(nums_to_delete):
    min_num = min(numbers_list)
    numbers_list.remove(min_num)

for numbers in range(len(numbers_list)):
    numbers_list[numbers] = str(numbers_list[numbers])
print(', '.join(numbers_list))
