line1 = input().split(' ')
line2 = input().split(' ')
line3 = input().split(' ')
list_all_combinations = [line1, line2, line3,
                         [line1[0], line2[1], line3[2]],
                         [line1[2], line2[1], line3[0]]]
for i in range(3):
    list_all_combinations.append([line1[i], line2[i], line3[i]])

for combination in list_all_combinations:
    if combination.count('1') == 3:
        print("First player won")
        break
    elif combination.count('2') == 3:
        print("Second player won")
        break
else:
    print("Draw!")