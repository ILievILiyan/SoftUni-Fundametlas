key_password = input()

while True:
    command = input()
    if command == "Generate":
        print(f'Your activation key is: {key_password}')
        break

    cmd = command.split(">>>")
    if cmd[0] == "Contains":
        substring = cmd[1]
        if substring in key_password:
            print(f'{key_password} contains {substring}')
        else:
            print('Substring not found!')
    elif cmd[0] == "Flip":
        type_text, start_index, end_index = cmd[1].lower(), int(cmd[2]), int(cmd[3])

        left_part = key_password[:start_index]
        center_part = key_password[start_index:end_index]
        right_part = key_password[end_index:]

        if type_text == "lower":
            center_part = center_part.lower()
        elif type_text == "upper":
            center_part = center_part.upper()
        key_password = left_part + center_part + right_part
        print(key_password)

    elif cmd[0] == "Slice":
        start_index, end_index = int(cmd[1]), int(cmd[2])
        key_password = key_password[:start_index] + key_password[end_index:]
        print(key_password)
