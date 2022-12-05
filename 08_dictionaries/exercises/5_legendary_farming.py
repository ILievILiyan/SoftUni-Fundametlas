data = input().split()
my_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk_materials = {}
game_won = False

while not game_won:
    for i in range(0, len(data), 2):
        material = data[i+1].lower()
        quantity = int(data[i])

        if material in my_materials.keys():
            my_materials[material] += quantity
            if my_materials[material] >= 250:
                my_materials[material] -= 250
                item = None
                if material == "shards":
                    item = "Shadowmourne"
                elif material == "fragments":
                    item = "Valanyr"
                elif material == "motes":
                    item = "Dragonwrath"
                print(f"{item} obtained!")
                game_won = True
                break
        else:
            if material not in junk_materials.keys():
                junk_materials[material] = 0
            junk_materials[material] += quantity
    if game_won:
        break
    data = input().split()

if game_won:
    print(f'shards: {my_materials["shards"]}')
    print(f'fragments: {my_materials["fragments"]}')
    print(f'motes: {my_materials["motes"]}')
    for key, value in junk_materials.items():
        print(f"{key}: {value}")


