def memory_game(numbers):
    moves = 0
    won_game = False

    command = input()
    while command != "end":
        moves += 1
        command = command.split(" ")
        i_1 = int(command[0])
        i_2 = int(command[1])
        half = int(len(numbers) / 2)

        if i_1 != i_2 and 0 <= i_1 < len(numbers) and 0 <= i_2 < len(numbers):
            if numbers[i_1] == numbers[i_2]:
                print(f'Congrats! You have found matching elements - {numbers[i_1]}!')
                numbers.pop(min(i_1, i_2))
                numbers.pop(max(i_1, i_2) - 1)
            else:
                print('Try again!')
        else:
            numbers.insert(half, f'{-moves}a')
            numbers.insert(half, f'{-moves}a')
            print('Invalid input! Adding additional elements to the board')
        if len(numbers) == 0:
            print(f'You have won in {moves} turns!')
            won_game = True
            break
        command = input()

    if not won_game:
        print('Sorry you lose :(')
        print(*numbers)


list_numbers = [i for i in input().split(" ")]
memory_game(list_numbers)