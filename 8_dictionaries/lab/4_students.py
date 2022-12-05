command = input().split(":")
students = {}

while len(command) > 1:
    name, ID, course = command[0], command[1], command[2]

    if course not in students.keys():
        students[course] = []
    students[course].append(f"{name} - {ID}")
    command = input().split(":")

searched_course = command[0].replace("_", " ")

if searched_course in students.keys():
    print("\n".join(students[searched_course]))