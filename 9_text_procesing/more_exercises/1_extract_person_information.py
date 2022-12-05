number_of_lines = int(input())

for _ in range(number_of_lines):
    name = ""
    age = ""
    current_string = input().replace(" ", "")
    name_start = 0
    name_end = 0
    age_start = 0
    age_end = 0
    for index, char in enumerate(current_string):
        if char == "@" and "|" in current_string[index::]:
            name_start = index
        if char == "|":
            name_end = index
        name = current_string[(name_start+1):name_end]

        if char == "#" and "*" in current_string[index::]:
            age_start = index
        if char == "*":
            age_end = index
        age = current_string[(age_start+1):age_end]

    print(f"{name} is {int(age)} years old.")
