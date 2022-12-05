string1 = input()
string2 = input()
last_string = string1

for i in range(len(string2)):
    left_side = string2[:i+1]
    right_side = string1[i+1:]
    new_string = left_side + right_side
    if new_string == last_string:
        continue
    print(new_string)
    last_string = new_string

