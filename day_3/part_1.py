# sample.txt answer is 4361
from copy import deepcopy
from itertools import product


def print_map(_map):
    for line in _map:
        print("".join([str(x) for x in line]))


with open("input.txt") as f:
    lines = f.readlines()
    lines = [list(line.strip()) for line in lines]

    # Setup a "minesweeper" grid
    minesweeper = [["."] * len(lines[0]) for _ in range(len(lines))]
    debug_map = deepcopy(minesweeper)
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if not (char.isnumeric() or char == "."):
                debug_map[i][j] = char
                i_range = range(max(0, i - 1), min(len(lines), i + 2))
                j_range = range(max(0, j - 1), min(len(line), j + 2))
                for i2, j2 in product(i_range, j_range):
                    minesweeper[i2][j2] = "X"
                minesweeper[i][j] = char

    num_list = []
    for i, line in enumerate(lines):
        num = ""
        is_part = False
        for j, char in enumerate(line):
            debug_map[i][j] = char
            if char.isnumeric():
                num += char
                if minesweeper[i][j] == "X":
                    is_part = True
            elif num:
                if is_part:
                    num_list.append(int(num))
                    is_part = False

                num = ""

# print_map(debug_map)

print(sum(num_list))
