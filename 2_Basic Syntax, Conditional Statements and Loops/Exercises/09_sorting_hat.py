
command = input()
sorted_students = 0
total_students = 0
while command != "Welcome!":
    name_of_student = command
    total_students += 1
    if name_of_student == "Voldemort":
        print("You must not speak of that name!")
        break
    else:
        if len(name_of_student) < 5:
            print(f'{name_of_student} goes to Gryffindor.')
        elif len(name_of_student) == 5:
            print(f'{name_of_student} goes to Slytherin.')
        elif len(name_of_student) == 6:
            print(f'{name_of_student} goes to Ravenclaw.')
        elif len(name_of_student) > 6:
            print(f'{name_of_student} goes to Hufflepuff.')
        sorted_students += 1
    command = input()
if total_students == sorted_students:
    print('Welcome to Hogwarts.')
