data = input().split()
bakery = {}

for i in range(0, len(data), 2):
    key = data[i]
    value = int(data[i+1])
    bakery[key] = value

# bakery = {data[i]: int(data[i+1]) for i in range(0, len(data), 2)}
print(bakery)
