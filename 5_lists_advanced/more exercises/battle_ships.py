def battle_ships(rows):
    field_rows = []
    destroyed_ships = 0
    condition = False

    for i in range(rows):
        field_rows.append(list(map(int, input().split(" "))))

    attacks = list(map(str, input().split(" ")))

    for i in attacks:
        counter = 0
        column = int(i[2])
        if int(i[0]) == 0:
            condition = True
        elif int(i[0]) == 1:
            condition = True
        elif int(i[0]) == 2:
            condition = True
        elif int(i[0]) == 3:
            condition = True

        if condition:
            for row in field_rows:
                if counter == int(i[0]):
                    row[column] -= 1
                    if row[column] == 0:
                        destroyed_ships += 1
                counter += 1
                condition = False

    print(destroyed_ships)


rows_input = int(input())
battle_ships(rows_input)