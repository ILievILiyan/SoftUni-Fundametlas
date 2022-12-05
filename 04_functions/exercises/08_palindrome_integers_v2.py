def find_palindrome(num):
    if num == num[::-1]:
        return True


numbers_list = input().split(" ")
for number in numbers_list:
    if find_palindrome(number):
        print("True")
    else:
        print("False")
