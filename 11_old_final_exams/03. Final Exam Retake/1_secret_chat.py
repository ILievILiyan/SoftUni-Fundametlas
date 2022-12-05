message = input()

while True:
    command = input()
    if command == "Reveal":
        print(f'You have a new text message: {message}')
        break

    cmd = command.split(":|:")

    if cmd[0] == "InsertSpace":
        index = int(cmd[1])
        message = message[:index] + " " + message[index:]
        print(message)
    elif cmd[0] == "Reverse":
        substring = cmd[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            reverse = substring[::-1]
            message += reverse
            print(message)
        else:
            print('error')
    elif cmd[0] == "ChangeAll":
        substring, replacement = cmd[1], cmd[2]
        while substring in message:
            message = message.replace(substring, replacement)
        print(message)

