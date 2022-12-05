num_of_wagons = int(input())
wagons = [0] * num_of_wagons


while True:

    command = input().split(" ")

    if command[0] == "End":
        break
    currenct_command = command[0]
    if currenct_command == "add":
        num_of_people = int(command[1])
        wagons[-1] += num_of_people

    elif currenct_command == "insert":
        index = int(command[1])
        num_of_people = int(command[2])
        wagons[index] += num_of_people

    elif currenct_command == "leave":
        index = int(command[1])
        num_of_people = int(command[2])
        wagons[index] -= num_of_people

print(wagons)
