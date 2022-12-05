num_of_numbers = int(input())

CONSTANT_EVEN = 'even'
CONSTANT_ODD = 'odd'
CONSTANT_POSITIVE = 'positive'
CONSTANT_NEGATIVE = 'negative'

numbers = []
filtered_numbers = []


for _ in range (num_of_numbers):
    current_num = int(input())
    numbers.append(current_num)

command = input()

for number in numbers:
    filter_numbers = (
        (command == CONSTANT_EVEN and number % 2 == 0) or
        (command == CONSTANT_ODD and number % 2 != 0) or
        (command == CONSTANT_POSITIVE and number >= 0) or
        (command == CONSTANT_NEGATIVE and number < 0)
    )

    if filter_numbers:
        filtered_numbers.append(number)

print(filtered_numbers)




