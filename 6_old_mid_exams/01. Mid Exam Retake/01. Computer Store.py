command = input()
total_sum_of_products = 0
order_is_ok = True

while command != "special" and command != "regular":
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        command = input()
        continue
    total_sum_of_products += current_price

    command = input()

taxes = total_sum_of_products * 0.2
final_sum_with_taxes = total_sum_of_products + taxes

if final_sum_with_taxes <= 0:
    print('Invalid order!')
    order_is_ok = False

if command == "special":
    final_sum_with_taxes *= 0.9

if order_is_ok:
    print('Congratulations you\'ve just bought a new computer!')
    print(f'Price without taxes: {total_sum_of_products:.2f}$')
    print(f'Taxes: {taxes:.2f}$')
    print('-----------')
    print(f'Total price: {final_sum_with_taxes:.2f}$')
