input_data = input()
all_forces = {}

while input_data != "Lumpawaroo":
    user_exist = False
    if " | " in input_data:
        command = input_data.split(" | ")
        force_side, force_user = str(command[0]), str(command[1])

        if force_side not in all_forces.keys():
            all_forces[force_side] = []

        for sides in all_forces.keys():
            if force_user in all_forces[sides]:
                user_exist = True

        if not user_exist:
            all_forces[force_side].append(force_user)

    elif " -> " in input_data:
        command = input_data.split(" -> ")
        force_side, force_user = command[1], command[0]

        if force_side not in all_forces.keys():
            all_forces[force_side] = []

        for sides in all_forces.keys():
            if force_user in all_forces[sides]:
                user_exist = True

        if not user_exist:
            all_forces[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")
        else:
            for sides in all_forces.keys():
                if force_user in all_forces[sides]:
                    all_forces[sides].remove(force_user)

            all_forces[force_side].append(force_user)
            print(f"{force_user} joins the {force_side} side!")


    input_data = input()

for side in all_forces.keys():
    if len(all_forces[side]) > 0:
        print(f"Side: {side}, Members: {len(all_forces[side])}")
        for users in all_forces[side]:
            print(f"! {users}")
