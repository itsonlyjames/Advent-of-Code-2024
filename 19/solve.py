import re
from functools import lru_cache

from aocd import data

patterns, designs = data.split("\n\n")
patterns = patterns.split(", ")
pattern = "|".join(patterns)


@lru_cache(None)
def count(design):
    if not design:
        return 1
    total = 0
    for pattern in patterns:
        if design.startswith(pattern):
            total += count(design[len(pattern) :])
    return total


possible = 0
total = 0

for design in designs.splitlines():
    match = re.fullmatch(f"({pattern})+", design)
    if match:
        possible += 1
    total += count(design)


print(f"p1: {possible}, p2: {total}")
