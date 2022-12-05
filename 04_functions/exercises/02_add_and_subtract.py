def add_and_subtract(n1, n2, n3):
    def sum_numbers():
        return n1 + n2

    def subtract():
        return sum_numbers() - n3

    print(subtract())


num1 = int(input())
num2 = int(input())
num3 = int(input())

add_and_subtract(num1, num2, num3)
