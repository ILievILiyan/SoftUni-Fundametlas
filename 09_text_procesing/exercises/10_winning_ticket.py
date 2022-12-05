tickets = input().split(", ")
valid_ticket = True
list_with_win_combination = ['@', '#', '$', '^']
for ticket in tickets:
    if len(ticket) != 20:
        valid_ticket = False
        continue

    if valid_ticket:
        half_ticket = int(len(ticket) / 2)
        count = 0
        for current_symbol in ticket[half_ticket]:
            if current_symbol in list_with_win_combination:
                count += 1
                win_symbol = current_symbol




