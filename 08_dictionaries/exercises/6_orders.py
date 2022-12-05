data = input().split()
products = {}

while len(data) > 1:
    product, price, quantity = data[0], data[1], data[2]
    if product not in products.keys():
        products[product] = []
        products[product].append(price)
        products[product].append(int(quantity))
    else:
        products[product][0] = price
        products[product][1] += int(quantity)

    data = input().split()

for key, value in products.items():
    print(f"{key} -> {(float(value[0]) * float(value[1])):.2f}")
