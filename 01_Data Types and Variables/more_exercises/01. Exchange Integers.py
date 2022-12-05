num1 = int(input())
num2 = int(input())
new_num1 = ""
new_num2 = ""

new_num1, new_num2 = num2, num1

print(f'Before:'
      f'\na = {num1}'
      f'\nb = {num2}')
print(f'After:'
      f'\na = {new_num1}'
      f'\nb = {new_num2}')
