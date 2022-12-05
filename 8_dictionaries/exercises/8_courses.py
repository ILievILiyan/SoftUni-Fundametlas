command = input().split(" : ")
courses_dictionary = {}

while command[0] != "end":
    course_name = command[0]
    student_name = command[1]

    if course_name not in courses_dictionary.keys():
        courses_dictionary[course_name] = []
    courses_dictionary[course_name].append(student_name)

    command = input().split(" : ")

for course_name, registered_students in courses_dictionary.items():
    print(f"{course_name}: {len(courses_dictionary[course_name])}")
    for students in courses_dictionary[course_name]:
        print(f'-- {students}')
