numbers_list = (input()).split(' ')
new_list = []

for number in numbers_list:
    number = abs(float(number))
    new_list.append(number)

print(new_list)