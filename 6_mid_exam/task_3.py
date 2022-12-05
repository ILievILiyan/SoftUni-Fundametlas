text_input = input()
final_text = []

while text_input != "end":
    text_split = text_input.split(" ")
    command = text_split[0]
    message = text_split[1]
    if command == "Chat":
        final_text.append(message)
    elif command == "Delete":
        if message in final_text:
            final_text.remove(message)
    elif command == "Edit":
        new_message = text_split[2]
        if message in final_text:
            index_of_message = final_text.index(message)
            final_text[index_of_message] = new_message
    elif command == "Pin":
        if message in final_text:
            index_of_message = final_text.index(message)
            message_to_pin = final_text.pop(index_of_message)
            final_text.append(message_to_pin)
    elif command == "Spam":
        for i in range(1, len(text_split)):
            final_text.append(text_split[i])
    text_input = input()

for elements in final_text:
    print(elements)