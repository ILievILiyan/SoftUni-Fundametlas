stops = input()

while True:
    command = input()
    if command == "Travel":
        break

    cmd = command.split(":")

    if cmd[0] == "Add Stop":
        index, string = int(cmd[1]), cmd[2]
        if 0 <= index <= len(stops):
            stops = stops[:index] + string + stops[index:]
    elif cmd[0] == "Remove Stop":
        start_index, end_index = int(cmd[1]), int(cmd[2])
        if 0 <= start_index <= end_index < len(stops):
            stops = stops[:start_index] + stops[end_index + 1:]
    elif cmd[0] == "Switch":
        old_string, new_string = cmd[1], cmd[2]
        if old_string in stops:
            stops = stops.replace(old_string, new_string)
    print(stops)

print(f'Ready for world tour! Planned stops: {stops}')