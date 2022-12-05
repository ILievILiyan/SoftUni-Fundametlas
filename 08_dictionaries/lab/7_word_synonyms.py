num_of_words = int(input())
synonyms = {}

for words in range(num_of_words):
    current_word = input()
    current_synonym = input()

    if current_word not in synonyms.keys():
        synonyms[current_word] = []
    synonyms[current_word].append(current_synonym)

for key , value in synonyms.items():
    print(f"{key} - {', '.join(value)}")
