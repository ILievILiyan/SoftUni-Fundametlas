def chek_even_number(number):
    if number % 2 == 0:
        return True


numbers = input().split(" ")
numbers_list = [int(numbers[i]) for i in range(len(numbers))]
even_numbers_list = list(filter(chek_even_number, numbers_list))

print(even_numbers_list)

