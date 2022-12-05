word = input()

alphabet_list_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
new_list = []

for i in range(len(word)):
    if word[i] in alphabet_list_upper:
        new_list.append(i)
print(new_list)

