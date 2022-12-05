def make_upper_lower(password_, index_, command_):
    if 0 <= index_ < len(password):
        first_p = password_[:index_]
        to_change = password_[index_]
        last_p = password_[index_ + 1:]
        if to_change.isalpha():
            if command_ == "Upper":
                to_change = to_change.upper()
            elif command_ == "Lower":
                to_change = to_change.lower()
            password_ = first_p + to_change + last_p
    return password_


def insert_char(password_, index_, char_):
    if 0 <= index_ < len(password):
        password_ = list(password_)
        password_.insert(index_, char_)
        password_ = "".join(password_)
    return password_


def replace_char(password_, char_, value_):
    if char in password_:
        total_value = ord(char_) + value_
        new_symbol = chr(total_value)
        password_ = password_.replace(char_, new_symbol)
    return password_


def validation(password_):
    if len(password_) < 8:
        print(f'Password must be at least 8 characters long!')

    for letter in password_:
        if not letter.isalnum() and letter != "_":
            print('Password must consist only of letters, digits and _!')
            break

    count_upper = 0
    count_lower = 0
    count_digit = 0
    for letter in password_:
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


password = input()
while True:
    command = input()
    if command == "Complete":
        break
    command = command.split(" ")

    if command[0] == "Make":
        index = int(command[2])
        password = make_upper_lower(password, index, command[1])
        print(password)
    elif command[0] == "Insert":
        index, char = int(command[1]), command[2]
        password = insert_char(password, index, char)
        print(password)
    elif command[0] == "Replace":
        char, value = command[1], int(command[2])
        password = replace_char(password, char, value)
        print(password)
    elif command[0] == "Validation":
        validation(password)
