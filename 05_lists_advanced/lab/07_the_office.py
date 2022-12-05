employees_rate = list(map(int, input().split(" ")))

factor = int(input())

average = sum(employees_rate) / len(employees_rate)
above_average = list(filter(lambda x: x >= average, employees_rate))

if len(above_average) >= len(employees_rate) / 2:
    print(f'Score: {len(above_average)}/{len(employees_rate)}. Employees are happy!')
else:
    print(f'Score: {len(above_average)}/{len(employees_rate)}. Employees are not happy!')





