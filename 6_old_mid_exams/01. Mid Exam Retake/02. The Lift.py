people = int(input())
wagon_list = (input()).split(' ')
wagon_as_int = [int(wagon_list[i]) for i in range(len(wagon_list))]
# wagon_as_int = list(map(int, wagon_list))

full_wagons = False

for i in range(len(wagon_list)):
    while wagon_as_int[i] < 4 and people > 0:
        wagon_as_int[i] += 1
        people -= 1
    if sum(wagon_as_int) == (len(wagon_as_int) * 4):
        full_wagons = True
        break

if full_wagons and people > 0:
    print(f'There isn\'t enough space! {people} people in a queue!')
elif not full_wagons:
    print('The lift has empty spots!')

print(' '.join(map(str, wagon_as_int)))
