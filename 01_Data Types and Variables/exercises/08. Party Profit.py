group = int(input())
days = int(input())
coins_left = 0

for day in range(1, days+1):
    if day % 10 == 0:
        group -= 2
    if day % 15 == 0:
        group += 5
    if day % 3 == 0:
        coins_left -= group * 3
    if day % 5 == 0:
        coins_left += group * 20
        if day % 3 == 0:
            coins_left -= group * 2
    coins_left += 50
    coins_left -= 2 * group
print(f'{group} companions received {int(coins_left/group)} coins each.')