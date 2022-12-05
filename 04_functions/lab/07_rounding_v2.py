numbers = input().split(" ")
rounded_number = []

for number in numbers:
    number = round(float(number))
    rounded_number.append(number)
print(rounded_number)