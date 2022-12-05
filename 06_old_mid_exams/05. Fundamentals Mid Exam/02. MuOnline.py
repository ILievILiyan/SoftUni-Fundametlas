rooms_input = input().split('|')
string = []
health = 100
btc = 0
game_over = False

for room in rooms_input:
    room = room.split(" ")
    string.append(room)

for i in range(len(string)):
    command = string[i][0]
    value = int(string[i][1])

    if command == "potion":
        if health + value <= 100:
            increase_health = value
            health += value
        else:
            increase_health = 100 - health
            health = 100

        print(f'You healed for {increase_health} hp.')
        print(f'Current health: {health} hp.')

    elif command == "chest":
        btc += value
        print(f'You found {value} bitcoins.')
    else:
        health -= value
        if health > 0:
            print(f'You slayed {command}.')
        else:
            print(f'You died! Killed by {command}.')
            print(f'Best room: {i + 1}')
            game_over = True
            break

if not game_over:
    print(f"You've made it!")
    print(f'Bitcoins: {btc}')
    print(f'Health: {health}')
