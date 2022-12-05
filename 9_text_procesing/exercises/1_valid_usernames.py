def valid_username(name):
    correct_name = False

    if 3 <= len(name) <= 16:
        correct_name = True
        for ch in name:
            if not ch.isalnum() and ch != "-" and ch != "_":
                correct_name = False
                break
    return correct_name


usernames = input().split(", ")
for name in usernames:
    if valid_username(name):
        print(name)
