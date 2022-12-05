numbers = int(input())
sum_of_digit = 0
for number in range(1, numbers + 1):
    sum_of_digit = 0
    digits = 0
    str_digits = ""
    for i in range(len(str(number))):
        str_number = str(number)
        str_digits = str_number[i]
        digits += int(str_digits)
    if digits == 5 or digits == 7 or digits == 11:
        print(f'{number} -> True')
    else:
        print(f'{number} -> False')