def length_of_username(name):
    if 3 <= len(name) <= 16:
        return True
    return False


def valid_symbols(name):
    for ch in name:
        if not ch.isalnum() and ch != "-" and ch != "_":
            return False
    return True


def validation_username(name):
    if length_of_username(name) and valid_symbols(name):
        return True
    return False


usernames = input().split(", ")
for name in usernames:
    if validation_username(name):
        print(name)
