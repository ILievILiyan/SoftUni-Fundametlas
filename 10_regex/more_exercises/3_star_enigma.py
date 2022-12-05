import re
num_of_msg = int(input())
decrypt_pattern = r"([starSTAR])"
is_correct_msg_pattern = r'@([A-Za-z]+)[^\@\-\!\:\>]*:(\d+)[^\@\-\!\:\>]*\!(A|D)\![^\@\-\!\:\>]*\->(\d+).*'

planets_attacks_dictionary = {"A" : [], "D": []}

for msg in range(num_of_msg):
    current_msg = input()
    decrypt_msg = ""
    decrypt_words = re.findall(decrypt_pattern, current_msg)
    ascii_num_of_char_back = len(decrypt_words)

    for char in current_msg:
        decrypt_msg += chr(ord(char) - ascii_num_of_char_back)

    correct_msg = re.search(is_correct_msg_pattern, decrypt_msg)
    if correct_msg:
        planet, population, attack_type, soldiers = correct_msg.groups()

        if attack_type not in planets_attacks_dictionary.keys():
            planets_attacks_dictionary[attack_type] = []
        planets_attacks_dictionary[attack_type].append(planet)

print(f'Attacked planets: {len(planets_attacks_dictionary["A"])}')
for planet in sorted(planets_attacks_dictionary['A']):
    print(f'-> {planet}')
print(f'Destroyed planets: {len(planets_attacks_dictionary["D"])}')
for planet in sorted(planets_attacks_dictionary['D']):
    print(f'-> {planet}')
