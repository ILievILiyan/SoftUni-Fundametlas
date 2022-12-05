string = input().split(" ")
new_string = [word for word in string if len(word) % 2 == 0]

print('\n'.join(new_string))

