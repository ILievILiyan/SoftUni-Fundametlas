numbers = list(map(int, input().split(", ")))

positives = [elements for elements in numbers if elements >= 0]
negatives = [elements for elements in numbers if elements < 0]
odds = [elements for elements in numbers if elements % 2 != 0]
evens = [elements for elements in numbers if elements % 2 == 0]

print(f'Positive: {", ".join(map(str, positives))}')
print(f'Negative: {", ".join(map(str, negatives))}')
print(f'Even: {", ".join(map(str, evens))}')
print(f'Odd: {", ".join(map(str, odds))}')
