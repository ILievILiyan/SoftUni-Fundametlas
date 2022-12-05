people = int(input())
capacity = int(input())

courses = 0

while people > 0:
    people -= capacity
    courses += 1

if people < 0 and courses > 1:
    print(f'{courses}')
elif people == 0:
    print(f'{courses}')
else:
    print(f'{courses}')