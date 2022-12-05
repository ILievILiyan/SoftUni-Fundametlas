def find_palindrome(num):
    for i in range(len(num)):
        if num[i-1] != num[-i]:
            return False
        else:
            return True


numbers_list = input().split(" ")
for number in numbers_list:
    print(find_palindrome(number))

    if find_palindrome(number):
        print("True")
    else:
        print("False")

