command = input().split("-")
data_students = {}
data_courses = {}

while len(command) > 1:
    username, language = command[0], command[1]

    if language != "banned":
        points = int(command[2])
        if language not in data_courses.keys():
            data_courses[language] = 0
        data_courses[language] += 1
        if username not in data_students.keys():
            data_students[username] = 0

        if points > data_students[username]:
            data_students[username] = points
    else:
        if username in data_students.keys():
            del data_students[username]

    command = input().split("-")

print("Results:")
for name, value in data_students.items():
    print(f"{name} | {value}")

print("Submissions:")
for key, value in data_courses.items():
    print(f"{key} - {value}")
