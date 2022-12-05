import re
players = input().split(", ")

pattern_name = r'([a-zA-Z]+)'
pattern_points = r'\d'

players_dict = {players[i]: 0 for i in range(0, len(players))}

while True:
    current_input = input()
    if current_input == "end of race":
        break

    current_winner = re.findall(pattern_name, current_input)
    current_points = re.findall(pattern_points, current_input)
    current_winner_name = "".join(current_winner)
    current_distance = sum(map(int, current_points))

    if current_winner_name in players_dict.keys():
        players_dict[current_winner_name] += current_distance

sorted_winners = dict(sorted(players_dict.items(), key=lambda x: (-x[1])))
print(f'1st place: {list(sorted_winners)[0]}')
print(f'2nd place: {list(sorted_winners)[1]}')
print(f'3rd place: {list(sorted_winners)[2]}')