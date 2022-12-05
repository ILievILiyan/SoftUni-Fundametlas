numbers_list = input().split(' ')
kill_count = int(input())
counter = 0
result = []

index = 0
while len(numbers_list) > 0:
    counter += 1

    if counter % kill_count == 0:
        result.append(numbers_list.pop(index))
    else:
        index += 1

    if index >= len(numbers_list):
        index = 0

print(str(result).replace(' ', '').replace('\'', ''))
