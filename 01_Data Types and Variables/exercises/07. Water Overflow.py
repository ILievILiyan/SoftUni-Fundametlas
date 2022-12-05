lines = int(input())
capacity_of_tank = 255
water_in_tank = 0
added_water = 0
for i in range(lines):
    water_to_add = int(input())
    while water_in_tank <= capacity_of_tank:
        if capacity_of_tank >= water_to_add:
            capacity_of_tank -= water_to_add
            added_water += water_to_add
        else:
            print('Insufficient capacity!')
        break
print(added_water)
