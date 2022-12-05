from string import ascii_lowercase
letters = {letter: str(index) for index, letter in enumerate(ascii_lowercase, start=1)}


def alphabet_position(char):
    number = letters[char.lower()]
    return number


string = input().split()
final_num = 0
for current_string in string:
    num = int(current_string[1:-1])
    if current_string[0].isupper():
        final_num += num / int(alphabet_position(current_string[0]))
    else:
        final_num += num * int(alphabet_position(current_string[0]))

    if current_string[-1].isupper():
        final_num -= int(alphabet_position(current_string[-1]))
    else:
        final_num += int(alphabet_position(current_string[-1]))

print(f"{final_num:.2f}")