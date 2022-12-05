cards = (input()).split(' ')
num_shuffles = int(input())

left_part = []
right_part = []
half = int(len(cards) / 2)

for shuffles in range(num_shuffles):
    current_cards = []
    left_part = cards[:half]
    right_part = cards[half::]

    for card in range(half):
        current_cards.append(left_part[card])
        current_cards.append(right_part[card])
    cards = current_cards

print(cards)
