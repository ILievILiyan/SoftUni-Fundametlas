numbers = input().split(", ")
numbers_list = list(map(int, numbers))

even_numbers_indexes = [index for index in range(len(numbers_list)) if numbers_list[index] % 2 == 0]
print(even_numbers_indexes)