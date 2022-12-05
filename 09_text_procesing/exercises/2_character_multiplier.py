string1, string2 = input().split()
common_len = min(len(string1), len(string2))
longer_string = max(len(string1), len(string2))

total_sum = 0

for ch in range(common_len):
    total_sum += ord(string1[ch]) * ord(string2[ch])

if len(string1) == longer_string:
    for ch in range(common_len, longer_string):
        total_sum += ord(string1[ch])
else:
    for ch in range(common_len, longer_string):
        total_sum += ord(string2[ch])


print(total_sum)






