num_of_rooms = int(input())
free_chairs = 0

for rooms in range(1, num_of_rooms + 1):
    command = input().split(" ")
    current_chairs = int(command[0].count("X"))
    visitors = int(command[1])
    free_chairs += current_chairs - visitors
    if current_chairs < visitors:
        print(f'{abs(current_chairs - visitors)} more chairs needed in room {rooms}')

if free_chairs >= 0:
    print(f'Game On, {free_chairs} free chairs left')