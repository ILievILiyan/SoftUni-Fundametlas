numbers = input().split(" ")
numbers_list = [int(numbers[i]) for i in range(len(numbers))]

even_numbers = list(filter(lambda x: (x % 2 == 0), numbers_list))
print(even_numbers)