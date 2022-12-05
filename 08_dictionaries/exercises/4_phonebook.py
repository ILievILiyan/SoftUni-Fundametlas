contacts = input().split("-")
contacts_dictionary = {}

while len(contacts) == 2:
    name, phone = contacts[0], contacts[1]
    contacts_dictionary[name] = phone

    contacts = input().split("-")

num_of_calls = int(contacts[0])
for i in range(num_of_calls):
    current_name = input()

    if current_name in contacts_dictionary.keys():
        print(f'{current_name} -> {contacts_dictionary[current_name]}')
    else:
        print(f"Contact {current_name} does not exist.")
