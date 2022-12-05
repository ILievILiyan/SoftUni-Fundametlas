input_line1 = (input()).split(' ')
input_line2 = (input()).split(' ')
input_line3 = (input()).split(' ')
line_1_int = [int(input_line1[i]) for i in range(len(input_line1))]
line_2_int = [int(input_line2[i]) for i in range(len(input_line2))]
line_3_int = [int(input_line3[i]) for i in range(len(input_line3))]


def winner(player):
    if line_1_int[0] == line_1_int[1] == line_1_int[2] == player or \
            line_2_int[0] == line_2_int[1] == line_2_int[2] == player or \
            line_3_int[0] == line_3_int[1] == line_3_int[2] == player or \
            line_1_int[0] == line_2_int[0] == line_3_int[0] == player or \
            line_1_int[1] == line_2_int[1] == line_3_int[1] == player or \
            line_1_int[2] == line_2_int[2] == line_3_int[2] == player or \
            line_1_int[0] == line_2_int[1] == line_3_int[2] == player or \
            line_1_int[2] == line_2_int[1] == line_3_int[0] == player:
        return winner


if winner(1):
    print('First player won')
elif winner(2):
    print("Second player won")
else:
    print('Draw!')
