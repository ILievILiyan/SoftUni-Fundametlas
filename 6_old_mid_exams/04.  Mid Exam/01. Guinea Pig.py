food = float(input())
hay = float(input())
cover = float(input())
pig_weight = float(input())

still_have_provisions = True

for day in range(1, 31):
    food -= 0.3
    if day % 2 == 0:
        hay -= 0.05 * food
    if day % 3 == 0:
        cover -= pig_weight / 3

    if food < 0.3 or hay <= 0 or cover <= 0:
        still_have_provisions = False
        break

if still_have_provisions:
    print(f'Everything is fine! Puppy is happy! Food: {food:.2f}, Hay: {hay:.2f}, Cover: {cover:.2f}.')
else:
    print('Merry must go to the pet store!')
