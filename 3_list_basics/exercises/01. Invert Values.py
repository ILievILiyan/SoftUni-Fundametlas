string = input()

new_list = string.split(" ")
new_list1 = []
for i in range(len(new_list)):
    new_element = -int(new_list[i])
    new_list1.append(new_element)
print(new_list1)