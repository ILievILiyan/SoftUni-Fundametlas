import re
total_price = 0
pattern = r'%([A-Z]{1}[a-z]+)%\D*<(\w+)>\D*\|(\d+)\|\D*(\d+\.?\d*)\$'

while True:
    text = input()
    if text == "end of shift":
        break

    current_order = re.search(pattern, text)

    if current_order:
        name, product, quantity, price = current_order.groups()
        current_price = int(quantity) * float(price)
        total_price += current_price
        print(f'{name}: {product} - {current_price:.2f}')

print(f'Total income: {total_price:.2f}')


