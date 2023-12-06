with open("input.txt") as f:
    lines = f.readlines()
from math import ceil, floor

times, records = (
    list(map(int, lines[0].split(":")[1].strip().split())),
    list(map(int, lines[1].split(":")[1].strip().split())),
)

num_ways_product = 1
for time, record in zip(times, records):
    _time = -time
    discriminant = _time**2 - 4 * record
    if discriminant < 0:
        print("No solution")
        continue

    h2 = (-_time + discriminant**0.5) / 2
    h1 = (-_time - discriminant**0.5) / 2

    num_ways = 0
    if h1 == ceil(h1):
        num_ways -= 1

    num_ways += ceil(h2) - ceil(h1)
    num_ways_product *= num_ways

print(num_ways_product)
