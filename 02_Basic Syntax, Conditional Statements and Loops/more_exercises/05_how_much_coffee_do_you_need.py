coffees_count = 0
list_commands_lower = ["coding", "dog", "cat", "movie"]
list_commands_upper = ["CODING", "DOG", "CAT", "MOVIE"]

command = input()
while command != "END":
    if command in list_commands_lower:
        coffees_count += 1
    elif command in list_commands_upper:
        coffees_count += 2
    command = input()

if coffees_count > 5:
    print('You need extra sleep')
else:
    print(f'{coffees_count}')