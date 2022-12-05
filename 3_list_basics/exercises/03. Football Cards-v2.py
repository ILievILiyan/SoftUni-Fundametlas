players_with_cards = (input()).split(' ')

list_a = ["A" + "-" + str(i) for i in range(1, 12)]
list_b = ["B" + "-" + str(i) for i in range(1, 12)]

game_was_terminated = False

for player in players_with_cards:
    if player in list_a:
        list_a.remove(player)
    elif player in list_b:
        list_b.remove(player)

    if len(list_a) < 7 or len(list_b) < 7:
        game_was_terminated = True
        break

print(f'Team A - {len(list_a)}; Team B - {len(list_b)}')
if game_was_terminated:
    print('Game was terminated')