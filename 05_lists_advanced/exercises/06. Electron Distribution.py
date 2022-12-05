electrons = int(input())
list_shell = []
n = 0

while electrons > 0:
    n += 1
    current_shell = 2 * (n ** 2)
    if electrons >= current_shell:
        list_shell.append(current_shell)
        electrons -= current_shell
    else:
        list_shell.append(electrons)
        electrons = 0
        break

print(list_shell)