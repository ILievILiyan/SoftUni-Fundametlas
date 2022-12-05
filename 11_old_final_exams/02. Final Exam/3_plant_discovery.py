num_of_plants = int(input())

plants = {}

for _ in range(num_of_plants):
    text = input().split('<->')
    plant, rarity = text[0], int(text[1])

    if plant not in plants.keys():
        plants[plant] = []
        plants[plant].append(rarity)
    else:
        plants[plant][0] = rarity

while True:
    command = input()
    if command == "Exhibition":
        break
    cmd = command.split(": ")

    if cmd[0] == "Rate":
        plant_rating = cmd[1].split(" - ")
        plant, rating = plant_rating[0], int(plant_rating[1])
        #rarity = #0 of list and #1 is rating in of list
        if plant not in plants.keys():
            print("error")
        else:
            plants[plant].append(rating)

    elif cmd[0] == "Update":
        plant_new_rarity = cmd[1].split(" - ")
        plant, new_rarity = plant_new_rarity[0], int(plant_new_rarity[1])
        if plant not in plants.keys():
            print("error")
        else:
            plants[plant][0] = new_rarity

    elif cmd[0] == "Reset":
        plant = cmd[1]
        if plant not in plants.keys():
            print("error")
        else:
            del plants[plant][1::]

print('Plants for the exhibition:')
for plant, rarity_points in plants.items():
    sum_ratings = sum(rarity_points[1::])
    length = len(rarity_points[1::])
    if sum != 0 and length != 0:
        average_rating = sum_ratings / len(rarity_points[1::])
    else:
        average_rating = 0
    print(f'- {plant}; Rarity: {rarity_points[0]}; Rating: {average_rating:.2f}')
