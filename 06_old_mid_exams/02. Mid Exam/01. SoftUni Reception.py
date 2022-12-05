students_per_hour_1 = int(input())
students_per_hour_2 = int(input())
students_per_hour_3 = int(input())
total_students = int(input())

total_answers_per_hour = students_per_hour_1 + students_per_hour_2 + students_per_hour_3
total_hours = 0

while total_students > 0:
    total_hours += 1
    if total_hours % 4 != 0:
        total_students -= total_answers_per_hour

print(f'Time needed: {total_hours}h.')
