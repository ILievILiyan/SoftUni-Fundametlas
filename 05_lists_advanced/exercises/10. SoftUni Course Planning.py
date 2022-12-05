schedule = input().split(", ")

while True:
    command = input()

    if command == "course start":
        break

    cmd_split = command.split(":")
    act = cmd_split[0]
    lesson = cmd_split[1]
    if len(cmd_split) > 2:
        lesson2 = cmd_split[2]

    if act == "Add" and lesson not in schedule:
        schedule.append(lesson)
    elif act == "Insert" and lesson not in schedule:
        idx = int(cmd_split[2])
        schedule.insert(idx, lesson)
    elif act == "Remove" and lesson in schedule:
        schedule.remove(lesson)
        while f'{lesson}-Exercise' in schedule:
            schedule.remove(f'{lesson}-Exercise')
    elif act == "Swap":
        if lesson in schedule and lesson2 in schedule:
            idx_lesson = schedule.index(lesson)
            idx_lesson2 = schedule.index(lesson2)
            schedule[idx_lesson], schedule[idx_lesson2] = schedule[idx_lesson2], schedule[idx_lesson]
            if f'{lesson}-Exercise' in schedule:
                while f'{lesson}-Exercise' in schedule:
                    schedule.remove(f'{lesson}-Exercise')
                schedule.insert(idx_lesson2 + 1, f'{lesson}-Exercise')
            if f'{lesson2}-Exercise' in schedule:
                while f'{lesson2}-Exercise' in schedule:
                    schedule.remove(f'{lesson2}-Exercise')
                schedule.insert(idx_lesson + 1, f'{lesson2}-Exercise')
    elif act == "Exercise":
        if lesson not in schedule:
            schedule.append(lesson)
            schedule.append(f'{lesson}-Exercise')
        else:
            idx_of_lesson = schedule.index(lesson)
            if f'{lesson}-Exercise' not in schedule:
                schedule.insert(idx_of_lesson + 1, f'{lesson}-Exercise')

for indexes, lessons in enumerate(schedule):
    print(f'{indexes + 1}.{lessons}')

