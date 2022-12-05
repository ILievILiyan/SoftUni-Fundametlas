words = {}
words_for_exam = {}

input_text = input().split(" | ")

for words_with_description in input_text:
    word_meaning = words_with_description.split(": ")
    if word_meaning[0] not in words.keys():
        words[word_meaning[0]] = []

    if word_meaning[1] not in words[word_meaning[0]]:
        words[word_meaning[0]].append(word_meaning[1])

current_word = input().split(" | ")
for word in current_word:
    if word in words.keys():
        if word not in words_for_exam.keys():
            words_for_exam[word] = []
        words_for_exam[word] = (words[word])

command = input()
if command == "Test":
    for word, definitions in words_for_exam.items():
        print(f'{word}:')
        for definition in definitions:
            print(f' -{definition}')

elif command == "Hand Over":
    print(f'{" ".join(words.keys())}')