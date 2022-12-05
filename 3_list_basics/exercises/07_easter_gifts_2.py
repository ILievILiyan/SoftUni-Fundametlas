gifts = input().split()
command = input()

while command != "No Money":
    command = command.split()

    if command[0] == "OutOfStock":
        for x in range(len(gifts)):
            if gifts[x] == command[1]:
                gifts[x] = None

    elif command[0] == "Required" and 0 <= int(command[2]) < len(gifts) :
        gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        gifts[-1] = command[1]

    command = input()

for gift in gifts:
    if gift is not None:
        print(gift, end=" ")