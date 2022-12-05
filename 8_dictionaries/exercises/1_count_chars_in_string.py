string = input().replace(" ", "")
chars_dictionary = {}

for i in range(len(string)):
    if string[i] not in chars_dictionary.keys():
        chars_dictionary[string[i]] = 0
    chars_dictionary[string[i]] += 1

for key,value in chars_dictionary.items():
    print(f"{key} -> {value}")

