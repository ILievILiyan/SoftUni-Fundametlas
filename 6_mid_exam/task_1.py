from math import ceil

budget = float(input())
students = int(input())
price_flour_package = float(input())
price_egg = float(input())
price_apron = float(input())

eggs_per_1_students = 10
flour_package_per_1_students = 1
apron_per_1_student = 1

total_expenses_apron = ceil(students * 1.2) * price_apron
total_expenses_eggs = eggs_per_1_students * price_egg * students
total_expenses_flour = (flour_package_per_1_students * students - flour_package_per_1_students * students //5)\
                       * price_flour_package

total_expenses = total_expenses_apron + total_expenses_flour + total_expenses_eggs


if budget >= total_expenses:
    print(f'Items purchased for {total_expenses:.2f}$.')
else:
    print(f'{abs(budget - total_expenses):.2f}$ more needed.')