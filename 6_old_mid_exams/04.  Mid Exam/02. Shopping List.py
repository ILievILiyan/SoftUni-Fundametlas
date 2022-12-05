product_list = input().split("!")

command = input()
while command != "Go Shopping!":
    command = command.split(" ")
    operation = command[0]
    item_1 = command[1]
    if operation == "Urgent":
        if item_1 not in product_list:
            product_list.insert(0, item_1)
    elif operation == "Unnecessary":
        if item_1 in product_list:
            product_list.remove(item_1)

    elif operation == "Correct":
        item_2 = command[2]
        if item_1 in product_list:
            for index in range(len(product_list)):
                if product_list[index] == item_1:
                    product_list[index] = item_2

    elif operation == "Rearrange":
        if item_1 in product_list:
            product_list.remove(item_1)
            product_list.insert(len(product_list), item_1)

    command = input()

x = ", ".join(map(str, product_list))
print(x)
