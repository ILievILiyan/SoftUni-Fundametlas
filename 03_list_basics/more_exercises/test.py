even_list = [2, 4, 6, 8, 10]
odd_list = [1, 3, 5, 7, 9]

e = input()

def max_min_even_odd(max_or_min, even_or_odd):
    if max_or_min == "max":
        max_or_min = max
    elif max_or_min == "min":
        max_or_min = min

    if even_or_odd == "even":
        even_or_odd = even_list
    elif even_or_odd == "odd":
        even_or_odd = odd_list

    if len(even_or_odd) > 0:
        return max_or_min(even_or_odd)
    else:
        return "empty"


print(max_min_even_odd(max, e))