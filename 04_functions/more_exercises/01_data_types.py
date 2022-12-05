def data_type(type_of_operation, operator):
    if type_of_operation == "int":
        return int(operator) * 2
    elif type_of_operation == "real":
        return f"{(float(operator) * 1.5):.2f}"
    elif type_of_operation == "string":
        return f'${operator}$'


current_type = input()
current_operator = input()
print(data_type(current_type,current_operator))