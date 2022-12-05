from math import ceil
numbers = list(map(int, input().split(", ")))
boundary = 0
new_list = []


for idx in range(ceil(max(numbers) / 10)):
    new_list.clear()
    boundary += 10
    for num in numbers:
        if num <= boundary:
            new_list.append(num)
    for elements in new_list:
        if elements in numbers:
            numbers.remove(elements)
    print(f"Group of {boundary}'s: {new_list}")
