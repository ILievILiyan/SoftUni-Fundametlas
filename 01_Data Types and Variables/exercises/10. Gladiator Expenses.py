lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price: float = float(input())
expenses = 0
shield_broken_count = 0

for fights in range(1, lost_fights + 1):
    if fights % 2 == 0:
        expenses += helmet_price
        if fights % 3 == 0:
            expenses += shield_price
            shield_broken_count += 1
    if fights % 3 == 0:
        expenses += sword_price

for shield_broken in range(1, shield_broken_count, 2):
    expenses += armor_price
print(f'Gladiator expenses: {expenses:.2f} aureus')

