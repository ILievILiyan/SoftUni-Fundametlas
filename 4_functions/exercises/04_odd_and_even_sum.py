def even_or_odd(number: str):
    even_sum = 0
    odd_sum = 0
    for elements in number:
        if int(elements) % 2 == 0:
            even_sum += elements
        else:
            odd_sum += elements
    return f'Odd sum = {odd_sum}, Even sum = {even_sum}'


entered_data = input()
print(even_or_odd(entered_data))
