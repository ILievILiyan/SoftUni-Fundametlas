data = input().split()
searched_products = input().split()

stocks = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = int(data[i+1])
    stocks[key] = value


for product in searched_products:
    if product in stocks.keys():
        print(f"We have {stocks[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")