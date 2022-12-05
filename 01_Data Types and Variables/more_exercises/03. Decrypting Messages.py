key = int(input())
num_of_lines = int(input())
password = ""
for nums in range(num_of_lines):
    char = input()
    password += chr(ord(char) + key)

print(password)

