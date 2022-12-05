quantity = int(input())
days_to_christmas = int(input())
spirit = 0
total_costs = 0

#prices
ornament_set_price = 2
tree_skirt_price = 5
tree_garland_price = 3
tree_lights_price = 15
#points
ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17


for day in range(1,days_to_christmas+1):
    if day % 11 == 0:
        quantity += 2
    if day % 2 == 0:
        total_costs += quantity * ornament_set_price
        spirit += ornament_set_points
    if day % 3 == 0:
        total_costs += quantity * (tree_skirt_price + tree_garland_price)
        spirit += tree_skirt_points + tree_garland_points
    if day % 5 == 0:
        total_costs += quantity * tree_lights_price
        spirit += tree_lights_points
        if day % 3 == 0:
            spirit += 30
    if day % 10 == 0:
        spirit -= 20
        total_costs += tree_skirt_price + tree_garland_price + tree_lights_price
if day % 10 == 0:
    spirit -= 30
print(f"Total cost: {total_costs}")
print(f"Total spirit: {spirit}")
