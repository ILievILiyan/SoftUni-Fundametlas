import re

total_price = 0
bought_items = []
search_pattern = r'>>([a-zA-Z]+)<<(\d+\.?\d*)!(\d+)'

while True:
    text = input()
    if text == "Purchase":
        break

    match = re.search(search_pattern, text)
    if match:
        furniture, price, quantity = match.groups()
        bought_items.append(furniture)
        total_price += float(price) * int(quantity)

print(f"Bought furniture:")
for furniture in bought_items:
    print(furniture)
print(f"Total money spend: {total_price:.2f}")
