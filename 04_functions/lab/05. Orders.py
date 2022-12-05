def calculator(product, quantity):
    if product == "coffee":
        return  quantity * 1.50
    elif product == "water":
        return quantity * 1
    elif product == "coke":
        return quantity * 1.40
    elif product == "snacks":
        return quantity * 2


product_order = input()
quantity_order = int(input())
result = calculator(product_order, quantity_order)
print(f'{result:.2f}')
