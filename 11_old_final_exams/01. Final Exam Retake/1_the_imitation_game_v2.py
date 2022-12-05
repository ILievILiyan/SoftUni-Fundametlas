def move(number_letters, message):
    text_to_move = message[:number_letters]
    message = message[number_letters:] + text_to_move
    return message


def insert(message, index_of_insert, value_of_insert):
    message = message[:index_of_insert] + value_of_insert + message[index_of_insert:]
    return message


def replace_text(message, substring_to_replace,  replacement_text):
    while substring in message:
        message = message.replace(substring_to_replace, replacement_text)
    return message


msg = input()

while True:
    command = input()
    if command == "Decode":
        print(f'The decrypted message is: {msg}')
        break

    cmd = command.split("|")

    if cmd[0] == "Move":
        num_letters = int(cmd[1])
        msg = move(num_letters, msg)

    elif cmd[0] == "Insert":
        index, value = int(cmd[1]), cmd[2]
        msg = insert(msg, index, value)

    elif cmd[0] == "ChangeAll":
        substring, replacement = cmd[1], cmd[2]
        msg = replace_text(msg, substring, replacement)

