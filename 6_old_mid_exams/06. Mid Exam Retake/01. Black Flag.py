days = int(input())
daily_plunder = int(input())
expected_plunber = float(input())
total_plunder = 0

for day in range(1, days + 1):
    total_plunder += daily_plunder
    if day % 3 == 0:
        total_plunder += 0.50 * daily_plunder
    if day % 5 == 0:
        total_plunder *= 0.7

if total_plunder >= expected_plunber:
    print(f'Ahoy! {total_plunder:.2f} plunder gained.')
else:
    result = (total_plunder / expected_plunber) * 100
    print(f'Collected only {result:.2f}% of the plunder.')
