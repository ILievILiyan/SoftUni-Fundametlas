num_of_char = int(input())
total_sum = 0

for index in range(num_of_char):
    char = input()
    total_sum += ord(char)
print(f'The sum equals: {total_sum}')

