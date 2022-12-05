def calculator(operator, n1, n2):
    if operator == "multiply":
        return int(n1 * n2)
    elif operator == "divide":
        return int(n1 / n2)
    elif operator == "add":
        return n1 + n2
    elif operator == "subtract":
        return n1 - n2


entered_operator = input()
number_1 = int(input())
number_2 = int(input())
print(calculator(entered_operator, number_1, number_2))
