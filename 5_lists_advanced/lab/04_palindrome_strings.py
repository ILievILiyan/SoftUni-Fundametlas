text = input().split(" ")
palindrome = input()

palindrome_list = [element for element in text if element == element[::-1]]
count = palindrome_list.count(palindrome)

print(palindrome_list)
print(f'Found palindrome {count} times')