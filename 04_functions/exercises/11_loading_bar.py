number = int(input())
progress = int(number // 10)

new_text = lambda a, b: a * b
if progress == 10:
    print('100% Complete!')
    print('[%%%%%%%%%%]')

else:
    final_result = "[" + new_text("%", progress) + new_text(".", 10 - progress) + "]"
    print(f'{number}% {final_result}')
    print('Still loading...')


