sequences_of_nums = input().split(" ")
numbers = [int(sequences_of_nums[i]) for i in range(len(sequences_of_nums))]
top_nums = []
average = sum(numbers) / len(numbers)

for i in range(5):
    current_max = max(numbers)
    if current_max > average:
        top_nums.append(current_max)
        numbers.remove(current_max)

if len(top_nums) > 0:
    result = " ".join(map(str, top_nums))
    print(result)
else:
    print("No")
