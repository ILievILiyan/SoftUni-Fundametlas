command = input().split(": ")
products = {}


while command[0] != "statistics":
    key = command[0]
    value = int(command[1])

    if key not in products.keys():
        products[key] = 0
    products[key] += value

    command = input().split(": ")


print("Products in stock:")
for product in products:
    print(f"- {product}: {products[product]}")
print(f"Total Products: {len(products)}")
print(f"Total Quantity: {sum(products.values())}")