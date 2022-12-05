energy = int(input())
count_wins = 0
game_lost = False

command = input()
while command != "End of battle":
    distance = int(command)
    if energy >= distance:
        energy -= distance
        count_wins += 1
    else:
        game_lost = True
        break

    if count_wins % 3 == 0:
        energy += count_wins
    command = input()

if game_lost:
    print(f'Not enough energy! Game ends with {count_wins} won battles and {energy} energy')
else:
    print(f'Won battles: {count_wins}. Energy left: {energy}')
