string = input().split(" ")
message = []

for i in range(len(string)):
    number = [number for number in string[i] if number.isdigit()]
    total_num = int("".join(map(str, number)))
    message.append(chr(total_num))
    chars = [chars for chars in string[i] if chars.isalpha()]
    chars[0], chars[-1] = chars[-1], chars[0]
    message.extend(chars)
    message.append(" ")
print("".join(message))
