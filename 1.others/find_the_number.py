import random

computer_number = random.randint(1, 100)
comp_num_found = False
my_num = int(input("Please submit a number between 1 and 100: "))

while not comp_num_found:
    if my_num > computer_number:
        my_num = int(input(f"Please submit a number lower than {my_num}: "))
    elif my_num < computer_number:
        my_num = int(input(f"Please submit a number higher than {my_num}: "))
    else:
        print(my_num)
        comp_num_found = True

