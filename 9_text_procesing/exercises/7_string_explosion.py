some_text = input()
new_text = ""
strength = 0

for i in range(len(some_text)):
    if strength > 0 and some_text[i] != ">":
        strength -= 1
    elif some_text[i] == ">":
        new_text += some_text[i]
        strength += int(some_text[i + 1])
    else:
        new_text += some_text[i]

print(new_text)
