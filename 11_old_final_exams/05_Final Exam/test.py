import re

pattern = r'(\@)(\#)+([A-Z][a-zA-Z0-9]{4,}[A-Z]{1})\1\2+'

products = []
num_of_strings = int(input())

for _ in range(num_of_strings):
    text = input()
    result = re.search(pattern, text)

    if not result:
        products.append("Invalid barcode")
    else:
        products.append(result.group(3))


for product in products:
    if product == "Invalid barcode":
        print(f'Invalid barcode')
        continue
    product_group = ""
    if product.isalpha():
        product_group = "00"
    else:
        for ch in product:
            if ch.isdigit():
                product_group += ch
    print(f'Product group: {product_group}')




