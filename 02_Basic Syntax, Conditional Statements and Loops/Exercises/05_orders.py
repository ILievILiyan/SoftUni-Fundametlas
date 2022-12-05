number_of_orders = int(input())
total_price = 0
order_is_ok = False

for orders in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        order_is_ok = True

    if order_is_ok:
        price_for_order = price_per_capsule * days * capsules_needed_per_day
        total_price += price_for_order
        print(f'The price for the coffee is: ${price_for_order:.2f}')
    else:
        continue
print(f'Total: ${total_price:.2f}')
