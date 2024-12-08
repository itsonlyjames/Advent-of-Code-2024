from aocd import data
from collections import defaultdict

grid = [list(line) for line in data.splitlines()]

def node_diff(a, b):
    return (a[0] - b[0], a[1] - b[1])

nodes = defaultdict(set)
INDICES = {}
for i, row in enumerate(data.strip().split("\n")):
    for j, c in enumerate(row):
        INDICES[(i, j)] = 0
        if c != ".":
            nodes[c].add((i, j))

uniq = set()
uniq2 = set()
for type, antennas in nodes.items():
    for a in antennas:
        uniq2.add(a)
        for b in antennas:
            if a == b:
                continue
            d = node_diff(a, b)
            try:
                node_ = (a[0] + d[0], a[1] + d[1])
                INDICES[node_]
                uniq.add(node_)
                uniq2.add(node_)
                while True:
                    node_ = (node_[0] + d[0], node_[1] + d[1])
                    INDICES[node_]
                    uniq2.add(node_)
            except KeyError:
                continue

print(len(uniq))
print(len(uniq2))
