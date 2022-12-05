input_data = input().split(" ")
targets = [int(input_data[i]) for i in range(len(input_data))]
# targets = list(map(int, input_tata))

shots = 0
targets_shot = []

command = input()
while command != "End":
    index = int(command)
    if index < len(targets):
        for num in range(len(targets)):
            if targets[num] > targets[index] and index != num:
                targets[num] -= targets[index]
            elif targets[index] >= targets[num] > 0 and index != num:
                targets[num] += targets[index]
        targets[index] = -1
        shots += 1
    else:
        command = input()
        continue
    command = input()

shot_targets = " ".join(map(str, targets))
print(f'Shot targets: {shots} -> {shot_targets}')

