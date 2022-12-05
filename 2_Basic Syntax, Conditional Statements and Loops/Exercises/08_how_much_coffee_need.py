coffee_you_need = 0
list_lowcase = ['coding', 'dog', 'cat', 'movie']
list_uppercase = ['CODING', 'DOG', 'CAT', 'MOVIE']
command = input()
while command != "END":
    if command in list_lowcase:
        coffee_you_need +=1
    if command in list_uppercase:
        coffee_you_need +=2
    command = input()

if coffee_you_need > 5:
    print('You need extra sleep')
else:
    print(coffee_you_need)
