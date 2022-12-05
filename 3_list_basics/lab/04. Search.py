num = int(input())
word = input()
my_list = []

for i in range(num):
    current_string = input()
    my_list.append(current_string)
print(my_list)

for i in range(len(my_list) -1, -1, -1):
    if word not in my_list[i]:
        my_list.remove(my_list[i])

print(my_list)
