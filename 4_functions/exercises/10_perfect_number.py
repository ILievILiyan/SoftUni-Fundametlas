def find_perfect_number(num):
    total_sum = 0
    for digit in range(1, num):
        if num % digit == 0:
            total_sum += digit

    if total_sum == num:
        return f'We have a perfect number!'
    else:
        return f'It\'s not so perfect.'


current_number = int(input())
print(find_perfect_number(current_number))
