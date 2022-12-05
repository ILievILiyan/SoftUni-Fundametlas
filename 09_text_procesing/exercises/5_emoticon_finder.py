text = input()

for index, ch in enumerate(text):
    if ch == ":":
        print(f"{ch}{text[index + 1]}")
