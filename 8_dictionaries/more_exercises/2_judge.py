exams = {}
names = {}
cmd = input().split(" -> ")
while cmd[0] != "no more time":
    username, contest, points = cmd[0], cmd[1], int(cmd[2])

    if contest not in exams.keys():
        exams[contest] = {}
        exams[contest][username] = 0

    if username not in exams[contest]:
        exams[contest][username] = 0

    if points > exams[contest][username]:
        exams[contest][username] = points
    cmd = input().split(" -> ")

for exam, name_points in exams.items():
    print(f"{exam}: {len(name_points.values())} participants")
    sorted_name_points = sorted(name_points.items(), key=lambda x: (-x[1], x[0]))
    count = 0
    for name, points in dict(sorted_name_points).items():
        if name not in names:
            names[name] = 0
        names[name] += points
        count += 1
        print(f"{count}. {name} <::> {points}")

print("Individual standings:")
sorted_individual_points = dict(sorted(names.items(), key=lambda x: (-x[1], x[0])))
count = 0
for name, points in sorted_individual_points.items():
    count += 1
    print(f"{count}. {name} -> {points}")
