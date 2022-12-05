def players_info(players, name, role, points):
    if name not in players:
        players[name] = {}
        players[name][role] = points
    else:
        if role not in players[name]:
            players[name][role] = points
        if players[name][role] < points:
            players[name][role] = points

    return players


def battles(players, p1, p2):
    for i in players[p1]:
        if i in players[p2]:
            if players[p1][i] > players[p2][i]:
                del players[p2]
                break
            elif players[p1][i] < players[p2][i]:
                del players[p1]
                break


def moba(seq):
    players = dict()
    while seq != "Season end":

        if '->' in seq:
            seq = seq.split(" -> ")
            name = seq[0]
            role = seq[1]
            points = int(seq[2])
            players_info(players, name, role, points)

        elif 'vs' in seq:
            seq = seq.split(" vs ")
            p1 = seq[0]
            p2 = seq[1]
            if p1 in players and p2 in players:
                battles(players, p1, p2)

        seq = input()

    for k, v in sorted(players.items(), key=lambda x: (-sum(x[1].values()), x[0])):
        print(f'{k}: {sum(v.values())} skill')
        for r, p in sorted(v.items(), key=lambda x: (-x[1], x[0])):
            print(f'- {r} <::> {p}')


sequence = input()
moba(sequence)