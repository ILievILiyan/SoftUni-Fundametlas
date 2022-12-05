input_data = input()
new_text = ""
text_to_copy = ""

for i, ch in enumerate(input_data):
    if not ch.isdigit():
        text_to_copy += ch.upper()
    else:
        if len(input_data) > i+1:
            if not input_data[i + 1].isdigit():
                new_text += text_to_copy * int(ch)
            elif input_data[i + 1].isdigit():
                new_text += text_to_copy * int(input_data[i] + input_data[i + 1])
            text_to_copy = ""
        else:
            new_text += text_to_copy * int(ch)

print(f"Unique symbols used: {len(set(new_text))}")
print(new_text)

