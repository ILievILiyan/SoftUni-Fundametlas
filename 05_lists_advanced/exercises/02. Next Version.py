version = input().split(".")
version_str = "".join(map(str, version))

version = str(int(version_str) + 1)
new_version_as_list = [version[index] for index in range(len(version))]

print(".".join(map(str, new_version_as_list)))