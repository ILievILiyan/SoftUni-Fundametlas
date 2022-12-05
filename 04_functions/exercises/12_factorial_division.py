def factorial_sum(num):
    for i in range(1, num):
        num *= i
    return num


number_1 = int(input())
number_2 = int(input())

result = factorial_sum(number_1) / factorial_sum(number_2)
print(f'{result:.2f}')
