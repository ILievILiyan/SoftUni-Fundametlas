first_text = input().split(", ")
second_text = input().split(", ")
new_string = []

for elements in first_text:
    for i in range(len(second_text)):
        if elements in second_text[i]:
            new_string.append(elements)
            break

print(new_string)