cars = input().split(">>")
total_taxes = 0

for car in range(len(cars)):
    car_type, years, km = cars[car].split(" ")

    if car_type == "family":
        car_tax = 50
        car_tax -= 5 * int(years)
        if int(km) >= 3000:
            car_tax += 12 * (int(km) // 3000)
    elif car_type == "heavyDuty":
        car_tax = 80
        car_tax -= 8 * int(years)
        if int(km) >= 9000:
            car_tax += 14 * (int(km) // 9000)
    elif car_type == "sports":
        car_tax = 100
        car_tax -= 9 * int(years)
        if int(km) >= 2000:
            car_tax += 18 * (int(km) // 2000)
    else:
        print(f'Invalid car type.')
        continue
    total_taxes += car_tax
    print(f'A {car_type} car will pay {car_tax:.2f} euros in taxes.')

print(f'The National Revenue Agency will collect {total_taxes:.2f} euros in taxes.')
