def symbols_between(start, end):
    new_list = []
    for i in range(ord(start) + 1, ord(end)):
        new_list.append(chr(i))
    return new_list


start_symbol = input()
end_symbol = input()
result = symbols_between(start_symbol, end_symbol)
print(" ".join(result))