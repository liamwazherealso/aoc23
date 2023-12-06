with open("input.txt") as f:
    lines = f.readlines()
from math import ceil


def line_to_int(line):
    return int("".join(line.split(":")[1].strip().split()))


time, record = list(map(line_to_int, lines))

num_ways_product = 1
_time = -time
discriminant = _time**2 - 4 * record
if discriminant < 0:
    print("No solution")
    exit()

h2 = (-_time + discriminant**0.5) / 2
h1 = (-_time - discriminant**0.5) / 2

num_ways = 0
if h1 == ceil(h1):
    num_ways -= 1

num_ways += ceil(h2) - ceil(h1)
num_ways_product *= num_ways

print(num_ways_product)
