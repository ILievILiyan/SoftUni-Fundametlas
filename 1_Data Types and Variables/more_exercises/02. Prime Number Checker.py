number = int(input())
is_prime = True

for index in range(2, number):
    if number % index == 0:
        is_prime = False
        break

if is_prime:
    print('True')
else:
    print('False')
