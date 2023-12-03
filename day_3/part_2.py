# sample.txt answer is 4361
from collections import defaultdict
from copy import deepcopy
from itertools import product


def print_map(_map):
    for line in _map:
        print("".join([str(x) for x in line]))


# sample.txt answer is 467835
with open("input.txt") as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]

    # Setup a "minesweeper" grid
    minesweeper = [["."] * len(lines[0]) for _ in range(len(lines))]

    connected_parts = defaultdict(list)

    debug_map = deepcopy(minesweeper)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if not (char.isnumeric() or char == "."):
                debug_map[i][j] = char
                i_range = range(max(0, i - 1), min(len(lines), i + 2))
                j_range = range(max(0, j - 1), min(len(line), j + 2))
                for i2, j2 in product(i_range, j_range):
                    minesweeper[i2][j2] = (i, j)
                minesweeper[i][j] = char

    for i, line in enumerate(lines):
        num = ""
        is_part = False
        for j, char in enumerate(line):
            debug_map[i][j] = char
            if char.isnumeric():
                num += char
                if minesweeper[i][j] != ".":
                    is_part = minesweeper[i][j]
            elif num:
                if is_part:
                    connected_parts[is_part].append(int(num))
                    is_part = False

                num = ""


gear_ratios = []
for connection_coor, part_list in connected_parts.items():
    if len(part_list) == 2:
        gear_ratios.append(part_list[0] * part_list[1])
print(sum(gear_ratios))
