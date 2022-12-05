def multiplication_sign(n1, n2, n3):
    negatives = []
    if n1 < 0:
        negatives.append(n1)
    if n2 < 0:
        negatives.append(n2)
    if n3 < 0:
        negatives.append(n3)

    if n1 == 0 or n2 == 0 or n3 == 0:
        print("zero")
    elif len(negatives) % 2 != 0:
        print("negative")
    else:
        print("positive")


num1 = int(input())
num2 = int(input())
num3 = int(input())

multiplication_sign(num1, num2, num3)
