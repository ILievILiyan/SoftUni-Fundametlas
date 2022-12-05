number = input()
numbers = str(number)

list_number = sorted(numbers, reverse=True)
for d, digit in enumerate(list_number):
    print(digit, end = "")


number = input()
numbers = str(number)

list_number = sorted(numbers, reverse=True)
print(''.join(list_number))