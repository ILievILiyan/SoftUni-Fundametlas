sequence_numbers = input().split(" ")
numbers_list = [int(sequence_numbers[i]) for i in range(len(sequence_numbers))]


min_number = min(numbers_list)
max_number = max(numbers_list)
sum_of_number = sum(numbers_list)

print(f'The minimum number is {min_number}')
print(f'The maximum number is {max_number}')
print(f'The sum number is: {sum_of_number}')