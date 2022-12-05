number_of_nums = int(input())
positive_list = []
negative_list = []
negative_sum = 0
for _ in range(number_of_nums):
    current_num = int(input())
    if current_num >= 0:
        positive_list.append(current_num)
    else:
        negative_list.append(current_num)
        negative_sum += current_num

print(f'{positive_list}'
      f'\n{negative_list}'
      f'\nCount of positives: {len(positive_list)}'
      f'\nSum of negatives: {negative_sum}')


