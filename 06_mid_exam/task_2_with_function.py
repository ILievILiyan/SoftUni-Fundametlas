def tax_calculator(start_tax, add_tax_years, car_years, additional_tax_km, car_kms, km_rates):
    car_taxes = start_tax
    car_taxes -= add_tax_years * int(car_years)
    if int(km) >= km_rates:
        car_taxes += additional_tax_km * (int(car_kms) // km_rates)
    return car_taxes


cars = input().split(">>")
total_taxes = 0

for car in range(len(cars)):
    car_type, years, km = cars[car].split(" ")

    if car_type == "family":
        car_tax = tax_calculator(50, 5, years, 12, km, 3000)
    elif car_type == "heavyDuty":
        car_tax = tax_calculator(80, 8, years, 14, km, 9000)
    elif car_type == "sports":
        car_tax = tax_calculator(100, 9, years, 18, km, 2000)
    else:
        print(f'Invalid car type.')
        continue
    total_taxes += car_tax
    print(f'A {car_type} car will pay {car_tax:.2f} euros in taxes.')
print(f'The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.')
