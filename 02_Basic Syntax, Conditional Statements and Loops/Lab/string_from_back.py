string = input()
new_string = ""

for char in range(len(string) -1, -1, -1):
    new_string += string[char]
print(new_string)

print(string[::-1])