number = int(input())


for first_num in range(number):
    for second_num in range(number):
        for third_num in range(number):
            print(f'{chr(97 + first_num)}{chr(97 + second_num)}{chr(97 + third_num)}')
