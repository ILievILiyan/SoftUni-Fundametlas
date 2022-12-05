password = input()

while True:
    command = input()
    if command == "Complete":
        break
    command = command.split(" ")

    if command[0] == "Make":
        index = int(command[2])
        if 0 <= index < len(password):
            first_part = password[:index]
            part_to_change = password[index]
            last_part = password[index+1:]
            if part_to_change.isalpha():
                if command[1] == "Upper":
                    part_to_change = part_to_change.upper()
                elif command[1] == "Lower":
                    part_to_change = part_to_change.lower()
                password = first_part + part_to_change + last_part
                print(password)

    elif command[0] == "Insert":
        index, char = int(command[1]), command[2]
        if 0 <= index < len(password):
            password = list(password)
            password.insert(index, char)
            password = "".join(password)
            print(password)

    elif command[0] == "Replace":
        char, value = command[1], int(command[2])
        if char in password:
            total_value = ord(char) + value
            new_symbol = chr(total_value)
            password = password.replace(char, new_symbol)
            print(password)

    elif command[0] == "Validation":
        if len(password) < 8:
            print(f'Password must be at least 8 characters long!')

        for letter in password:
            if not letter.isalnum() and letter != "_":
                print('Password must consist only of letters, digits and _!')
                break

        count_upper = 0
        count_lower = 0
        count_digit = 0
        for letter in password:
            if letter.isupper():
                count_upper += 1
            if letter.islower():
                count_lower += 1
            if letter.isdigit():
                count_digit += 1

        if count_upper < 1:
            print('Password must consist at least one uppercase letter!')
        if count_lower < 1:
            print('Password must consist at least one lowercase letter!')
        if count_digit < 1:
            print('Password must consist at least one digit!')

