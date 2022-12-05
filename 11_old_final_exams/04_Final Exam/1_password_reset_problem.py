password = input()


while True:
    command = input().split()
    if command[0] == "Done":
        print(f'Your password is: {password}')
        break

    elif command[0] == "TakeOdd":
        password = [password[i] for i in range(len(password)) if i% 2 != 0]
        password = "".join(password)
        print(password)

    elif command[0] == "Cut":
        index, length = int(command[1]), int(command[2])
        string_to_remove = password[index: index+length]
        password = password.replace(string_to_remove, "", 1 )
        print(password)
    elif command[0] == "Substitute":
        substring, substitute = command[1], command[2]
        if substring in password:
            password = password.replace(substring, substitute)
            print(password)
        else:
            print(f'Nothing to replace!')
