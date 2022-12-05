number_of_messages = int(input())

for i in range(1, number_of_messages +1):
    code_number = int(input())

    if code_number == 88:
        print('Hello')
    elif code_number == 86:
        print('How are you?')
    elif code_number < 88 and code_number != 86:
        print('GREAT!')
    else:
        print('Bye.')
