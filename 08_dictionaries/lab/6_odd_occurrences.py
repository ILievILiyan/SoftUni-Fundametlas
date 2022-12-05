words = input().split()
dictionary = {}

for word in words:
    word_lower = word.lower()

    if word_lower not in dictionary.keys():
        dictionary[word_lower] = 0
    dictionary[word_lower] += 1

for key, values in dictionary.items():
    if values % 2 != 0:
        print(key, end = " ")
