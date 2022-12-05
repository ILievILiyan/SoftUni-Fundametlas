from math import floor
budget = float(input())
price_for_kg_flour = float(input())

price_for_pack_eggs = price_for_kg_flour * 0.75
price_for_liter_milk = price_for_kg_flour * 1.25

pack_eggs_for_1_bread = 1
kg_flour_for_1_bread = 1
liters_milk_for_1_bread = 0.25
made_leaves = 0
total_colored_eggs = 0

total_price_for_1_bread = pack_eggs_for_1_bread * price_for_pack_eggs \
                          + kg_flour_for_1_bread * price_for_kg_flour \
                          + liters_milk_for_1_bread * price_for_liter_milk

while budget - total_price_for_1_bread >= 0:
    made_leaves += 1
    budget -= total_price_for_1_bread
    total_colored_eggs += 3
    if made_leaves % 3 == 0:
        total_colored_eggs -= (made_leaves - 2)

print(f'You made {made_leaves} loaves of Easter bread! Now you have {total_colored_eggs} eggs and {budget:.2f}BGN left.')







