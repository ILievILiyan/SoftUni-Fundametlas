
number = int(input())

for i in range(1, number+1):
    for j in range(1, i+1):
        print("*", end="")
    print()

for k in range(number-1, 0, -1):
    for m in range(0, k):
        print("*", end="")
    print()