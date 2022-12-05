num_of_grades = int(input())
students_grades = {}


for grades in range(num_of_grades):
    name = input()
    current_grade = float(input())

    if name not in students_grades.keys():
        students_grades[name] = []
    students_grades[name].append(current_grade)


for student,grade in students_grades.items():
    avg_grade = sum(grade) / len(grade)
    if avg_grade >= 4.50:
        print(f"{student} -> {avg_grade:.2f}")

