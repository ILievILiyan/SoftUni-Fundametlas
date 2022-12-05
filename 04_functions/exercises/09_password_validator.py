from string import digits, ascii_uppercase, ascii_lowercase
letters_list = ascii_lowercase + ascii_uppercase
digits_list = list(digits)
all_combination_password = digits + ascii_lowercase + ascii_uppercase


def is_password_ok(password):
    digit_counter = 0
    password_is_ok = True
    if len(password) > 10 or len(password) < 6:
        print('Password must be between 6 and 10 characters')
        password_is_ok = False
    for i in range(len(password)):
        if password[i] not in all_combination_password:
            print('Password must consist only of letters and digits')
            password_is_ok = False
            break
        if password[i] in digits_list:
            digit_counter += 1
    if digit_counter < 2:
        print('Password must have at least 2 digits')
        password_is_ok = False

    if password_is_ok:
        print('Password is valid')


current_password = input()
is_password_ok(current_password)
