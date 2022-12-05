items_input = input().split('|')
item_list = []
energy = 100
coins = 100
bought_items = 0
day_completed = True

for items in items_input:
    item = items.split("-")
    item_list.append(item)

for i in range(len(item_list)):
    current_value = int(item_list[i][1])
    current_item = item_list[i][0]

    if current_item == "rest":
        if energy + current_value > 100:
            gained_energy = 100 - energy
            energy = 100
        else:
            energy += current_value
            gained_energy = current_value
        print(f'You gained {gained_energy} energy.')
        print(f'Current energy: {energy}.')

    elif current_item == "order":
        if energy >= 30:
            energy -= 30
            coins += current_value
            print(f'You earned {current_value} coins.')
        else:
            energy += 50
            print(f'You had to rest!')
            continue
    else:
        if coins >= current_value:
            coins -= current_value
            print(f'You bought {current_item}.')
        else:
            print(f'Closed! Cannot afford {current_item}.')
            day_completed = False
            break
            
if day_completed:
    print(f'Day completed!')
    print(f'Coins: {coins}')
    print(f'Energy: {energy}')
