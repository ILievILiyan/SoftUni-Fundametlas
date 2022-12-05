def fire(ship_health, idx, dmg):
    if idx < len(ship_health):
        ship_health[idx] -= dmg
        if ship_health[idx] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
    return ship_health


def defend(ship_health, index1, index2, dmg):
    if 0 <= index1 < index2 < len(ship_health):
        for i in range(index1, index2 + 1):
            ship_health[i] -= dmg
            if ship_health[i] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    return ship_health


def repair(ship_health, idx, current_health, maximum_health):
    if idx < len(ship_health):
        ship_health[idx] += current_health
        if ship_health[idx] > maximum_health:
            ship_health[idx] = maximum_health
    return ship_health


def status(ship_health, maximum_health):
    count = 0
    for elements in ship_health:
        if elements < maximum_health * 0.2:
            count += 1
    return f'{count} sections need repair.'


pirate = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
max_health = int(input())

while True:
    command = input()
    if command == "Retire":
        break

    command_split = command.split(" ")
    cmd = command_split[0]

    if cmd == "Fire":
        index = int(command_split[1])
        damage = int(command_split[2])
        result = fire(warship, index, damage)

    elif cmd == "Defend":
        start_i = int(command_split[1])
        end_i = int(command_split[2])
        damage = int(command_split[3])
        result = defend(pirate, start_i, end_i, damage)

    elif cmd == "Repair":
        index = int(command_split[1])
        health = int(command_split[2])
        result = repair(pirate, index, health, max_health)

    elif cmd == "Status":
        result = status(pirate, max_health)
        print(result)

print(f"Pirate ship status: {sum(pirate)}")
print(f"Warship status: {sum(warship)}")
