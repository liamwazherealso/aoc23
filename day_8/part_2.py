from itertools import cycle

with open("input.txt") as f:
    lines = f.readlines()

directions = [int(c == "R") for c in lines[0].strip()]

nodes = {}
for line in lines[2:]:
    node, _, *path = line.strip().split()
    nodes[node] = [e.strip("(),") for e in path]


def find(start_node):
    node = start_node
    for step_count, direction in enumerate(cycle(directions), 1):
        node = nodes[node][direction]

        if node.endswith("Z"):
            return step_count


starting_nodes = [node for node, path in nodes.items() if node.endswith("A")]

step_counts = []

for starting_node in starting_nodes:
    step_counts.append(find(starting_node))

from math import lcm

print(lcm(*step_counts))
