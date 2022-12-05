string = input()

string = string.lower()
words_list = ['sand', 'water', 'fish', 'sun']
sum = 0

for item in words_list:
    if item in string:
        word_count = string.count(item)
        sum += word_count
print(sum)