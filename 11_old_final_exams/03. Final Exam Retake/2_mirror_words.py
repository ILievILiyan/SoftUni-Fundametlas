import re

text = input()

pattern = r'(\@|\#)([a-zA-Z]{3,})\1\1([a-zA-Z]{3,})\1'

result = re.findall(pattern, text)
final_result = []

for words in result:
    if words[1] == words[2][::-1]:
        final_result.append(f'{words[1]} <=> {words[2]}')

if len(result) > 0:
    print(f'{len(result)} word pairs found!')
else:
    print('No word pairs found!')

if len(final_result) > 0:
    print(f'The mirror words are:')
    print(f'{", ".join(final_result)}')
else:

    print('No mirror words!')