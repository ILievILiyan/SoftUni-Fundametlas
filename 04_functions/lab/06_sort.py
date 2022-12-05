sequence_numbers = input().split(" ")
numbers_list = [int(sequence_numbers[i]) for i in range(len(sequence_numbers))]

sorted_list = sorted(numbers_list)

print(sorted_list)