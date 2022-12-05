num_of_snowballs = int(input())

best_snowball = 0
value_of_current_snowball = 0

for player in range(2):
    for balls in range(num_of_snowballs):
        weight = int(input())
        time_to_target = int(input())
        quality = int(input())
        value_of_current_snowball = (weight / time_to_target) ** quality

        if value_of_current_snowball > best_snowball:
            best_snowball = value_of_current_snowball
            best_weight = weight
            best_time = time_to_target
            best_quality = quality
    break
print(f'{best_weight:.0f} : {best_time:.0f} = {best_snowball:.0f} ({best_quality:.0f})')

