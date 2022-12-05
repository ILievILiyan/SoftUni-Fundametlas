num_of_commands = int(input())
parking_data = {}

for commands in range(num_of_commands):
    current_cmd = input().split()
    cmd, username = current_cmd[0], current_cmd[1]
    if cmd == "register":
        license_plate_number = current_cmd[2]
        if username in parking_data.keys():
            print(f'ERROR: already registered with plate number {license_plate_number}')
        else:
            parking_data[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")

    elif cmd == "unregister":
        if username not in parking_data.keys():
            print(f'ERROR: user {username} not found')
        else:
            del parking_data[username]
            print(f"{username} unregistered successfully")

for name, numbers in parking_data.items():
    print(f"{name} => {numbers}")