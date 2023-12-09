from itertools import cycle

with open("input.txt") as f:
    lines = f.readlines()

directions = [int(c == "R") for c in lines[0].strip()]

nodes = {}
for line in lines[2:]:
    node, _, *path = line.strip().split()
    nodes[node] = [e.strip("(),") for e in path]


def find(start_node, end_node):
    node = start_node
    for step_count, direction in enumerate(cycle(directions), 1):
        node = nodes[node][direction]

        if node == end_node:
            return step_count


print(find("AAA", "ZZZ"))
