msg = input()

while True:
    command = input()
    if command == "Decode":
        break

    cmd = command.split("|")

    if cmd[0] == "Move":
        num_letters = int(cmd[1])
        text_to_move = msg[:num_letters]
        msg = msg[num_letters:] + text_to_move

    elif cmd[0] == "Insert":
        index = int(cmd[1])
        value = cmd[2]
        msg = msg[:index] + value + msg[index:]

    elif cmd[0] == "ChangeAll":
        substring = cmd[1]
        replacement = cmd[2]
        while substring in msg:
            msg = msg.replace(substring, replacement)

print(f'The decrypted message is: {msg}')