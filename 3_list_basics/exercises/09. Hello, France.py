item_with_price = (input()).split('|')
budget = float(input())
items_for_sale_list = []
bought_items = 0

for i in range(len(item_with_price)):
    item_with_price[i] = item_with_price[i].split('->')

for i in range(len(item_with_price)):
    if budget - float(item_with_price[i][1]) >= 0:
        if item_with_price[i][0] == "Clothes" and item_with_price[i][1] <= 50.00 or item_with_price[i][
            0] == "Shoes" and float(item_with_price[i][1]) <= 35.00 or item_with_price[i][0] == "Accessories" and \
                float(item_with_price[i][1]) <= 20.50:
            budget -= item_with_price[i][1]
            bought_items += item_with_price[i][1]
            items_for_sale_list.append(item_with_price[i][1] * 1.4)

items_for_sale = bought_items * 1.4
total_budget = budget + items_for_sale

for i in items_for_sale_list:
    print(f'{i:.2f}', end=' ')

print(f'\nProfit: {(items_for_sale - bought_items):.2f} ')
if total_budget >= 150:
    print(f'Hello, France!')
else:
    print("Not enough money.")
