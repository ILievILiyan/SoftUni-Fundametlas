count_a_cartons = 0
count_b_cartons = 0

input_data = (input()).split(' ')
set_with_cartons = {input_data[i] for i in range(len(input_data))}
list_with_cartons = list(set_with_cartons)

for i in range(len(list_with_cartons)):
    if "A" in list_with_cartons[i]:
        count_a_cartons += 1
        if count_a_cartons > 4:
            break
    elif "B" in list_with_cartons[i]:
        count_b_cartons += 1
        if count_a_cartons > 4:
            break
team_a_players = 11 - count_a_cartons
team_b_players = 11 - count_b_cartons

print(f'Team A - {team_a_players}; Team B - {team_b_players}')

if team_a_players < 7 or team_b_players < 7:
    print('Game was terminated')
