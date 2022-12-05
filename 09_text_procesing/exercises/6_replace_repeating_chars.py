text = list(input())
old_ch = ""

for index in range(len(text)):
    if text[index] == old_ch:
        text[index] = ""
        continue
    old_ch = text[index]

print("".join(text))