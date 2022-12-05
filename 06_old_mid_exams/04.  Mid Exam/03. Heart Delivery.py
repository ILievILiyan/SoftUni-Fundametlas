targets = input().split("@")
numbers = [int(targets[i]) for i in range(len(targets))]
index = 0

command = input()
while command != "Love!":
    command = command.split(" ")
    index += int(command[1])
    if index >= len(numbers):
        index = 0
    if numbers[index] == 0:
        print(f"Place {index} already had Valentine's day.")
    else:
        numbers[index] -= 2
        if numbers[index] == 0:
            print(f"Place {index} has Valentine's day.")
    command = input()

failed_places = len(numbers) - numbers.count(0)
print(f"Cupid's last position was {index}.")

if sum(numbers) == 0:
    print(f'Mission was successful.')
else:
    print(f'Cupid has failed {failed_places} places.')
