cmd1 = input().split(":")
contest_password_base = {}
contest_password_final = {}
final_print = {}
winner = None
names = []

while cmd1[0] != "end of contests":
    contest_base, password_base = cmd1[0], cmd1[1]
    contest_password_base[contest_base] = password_base
    cmd1 = input().split(":")

cmd2 = input().split("=>")
while cmd2[0] != "end of submissions":
    contest, password, username, points = cmd2[0], cmd2[1], cmd2[2], int(cmd2[3])
    if contest in contest_password_base.keys() and password == contest_password_base[contest]:
        if contest not in contest_password_final.keys():
            contest_password_final[contest] = {}
            contest_password_final[contest][username] = 0
        if username not in contest_password_final[contest].keys():
            contest_password_final[contest][username] = points

        if contest_password_final[contest][username] < points:
            contest_password_final[contest][username] = points
    cmd2 = input().split("=>")

for people_points in contest_password_final.values():
    for person, points in people_points.items():
        if person not in final_print.keys():
            final_print[person] = 0
        final_print[person] += points

for name, age in final_print.items():
    names.append(name)
    if age == max(final_print.values()):
        winner = name

print(f"Best candidate is {winner} with total {max(final_print.values())} points.")
print("Ranking:")

for name in sorted(names):
    final_dict = {}
    print(name)
    for exam, name_points in contest_password_final.items():
        for current_name, current_points in name_points.items():
            if current_name == name:
                final_dict[exam] = int(current_points)
    sorted_final_dict = dict(sorted(final_dict.items(), key=lambda x: -x[1]))
    for exam, final_score in sorted_final_dict.items():
        print(f"#  {exam} -> {final_score}")
