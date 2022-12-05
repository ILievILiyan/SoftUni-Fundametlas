new_list = []

while True:
    text = input()

    if text == "End":
        break
    split_command = text.split("-")
    priority = int(split_command[0])
    task = split_command[1]
    new_list.append((priority, task))

sorted_tasks = [task_data[1] for task_data in sorted(new_list)]
print(sorted_tasks)