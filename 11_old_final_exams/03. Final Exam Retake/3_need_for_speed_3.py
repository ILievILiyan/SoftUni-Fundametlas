def drive(cars_dictionary, car_, distance_, fuel_):
    if car_ in cars_dictionary.keys():
        split_mileage_fuel = cars_dictionary[car_].split(":")
        already_mileage = int(split_mileage_fuel[0])
        available_fuel = int(split_mileage_fuel[1])

        if available_fuel < fuel_:
            print("Not enough fuel to make that ride")
        else:
            already_mileage += distance_
            available_fuel -= fuel_
            cars_dictionary[car_] = str(already_mileage) + ":" + str(available_fuel)
            print(f'{car_} driven for {distance_} kilometers. {fuel_} liters of fuel consumed.')

        if already_mileage >= 100000:
            print(f'Time to sell the {car_}!')
            cars_dictionary.pop(car_)
    return cars_dictionary


def refuel(cars_dictionary, car_, fuel_):
    if car_ in cars_dictionary.keys():
        split_mileage_fuel = cars_dictionary[car_].split(":")
        already_mileage = int(split_mileage_fuel[0])
        available_fuel = int(split_mileage_fuel[1])

        if available_fuel + fuel_ > 75:
            print(f'{car_} refueled with {75 - available_fuel} liters')
            available_fuel = 75
        else:
            available_fuel += fuel_
            print(f'{car_} refueled with {fuel_} liters')
        cars_dictionary[car_] = str(already_mileage) + ":" + str(available_fuel)
    return cars_dictionary


def revert(cars_dictionary, car_, km_):
    if car_ in cars_dictionary.keys():
        split_mileage_fuel = cars_dictionary[car_].split(":")
        already_mileage = int(split_mileage_fuel[0])
        available_fuel = int(split_mileage_fuel[1])

        already_mileage -= int(km_)
        if already_mileage <= 10000:
            already_mileage = 10000
        else:
            print(f'{car_} mileage decreased by {km_} kilometers')
        cars_dictionary[car_] = str(already_mileage) + ":" + str(available_fuel)
    return cars_dictionary


number_of_cars = int(input())
cars = {}
for _ in range(number_of_cars):
    text = input().split("|")
    car, mileage, fuel = text[0], text[1], text[2]

    if car not in cars.keys():
        cars[car] = None
    cars[car] = mileage+":"+fuel
    # index0 = mileage; index1 = fuel

while True:
    command = input()
    if command == "Stop":
        break

    cmd = command.split(" : ")
    if cmd[0] == "Drive":
        car, distance, fuel = cmd[1], int(cmd[2]), int(cmd[3])
        drive(cars, car, distance, fuel)
    elif cmd[0] == "Refuel":
        car, fuel = cmd[1], int(cmd[2])
        refuel(cars, car, fuel)
    elif cmd[0] == "Revert":
        car, km = cmd[1], int(cmd[2])
        revert(cars, car, km)

for car, mileage_fuel in cars.items():
    current_split_mileage_fuel = mileage_fuel.split(":")
    current_already_mileage = int(current_split_mileage_fuel[0])
    current_available_fuel = int(current_split_mileage_fuel[1])
    print(f'{car} -> Mileage: {current_already_mileage} kms, Fuel in the tank: {current_available_fuel} lt.')
