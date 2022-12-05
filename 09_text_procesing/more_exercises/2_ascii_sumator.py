start = ord(input())
end = ord(input())
string = input()
total_sum = 0

for ch in string:
    if start < ord(ch) < end:
        total_sum += ord(ch)
print(total_sum)
