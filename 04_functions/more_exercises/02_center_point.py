def finding_closest_point(x1, y1, x2, y2):
    first_distance_to_center = pow(x1, 2) + pow(y1, 2)
    second_distance_to_center = pow(x2, 2) + pow(y2, 2)

    if first_distance_to_center <= second_distance_to_center:
        return f'({int(x1)}, {int(y1)})'
    else:
        return f'({int(x2)}, {int(y2)})'


x_1 = float(input())
y_1 = float(input())
x_2 = float(input())
y_2 = float(input())

print(finding_closest_point(x_1, y_1, x_2, y_2))
