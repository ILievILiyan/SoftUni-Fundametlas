array_input = input().split(" ")
array_list = [int(array_input[i]) for i in range(len(array_input))]

print(array_list)
print(type(array_list[1]))

x = ", ".join(map(str, array_list))

print(type(x[0]))