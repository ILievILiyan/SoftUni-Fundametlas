directory = input().split("\\")
file = directory[-1].split(".")
filename = file[0]
extension = file[1]

print(f"File name: {filename}")
print(f"File extension: {extension}")


