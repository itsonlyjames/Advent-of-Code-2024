from functools import cache

from aocd import data

@cache
def evolve_stones(start, blinks):
    if blinks == 0:
        return 1

    if start == 0:
        return evolve_stones(1, blinks - 1)
    elif len((s := str(start))) % 2 == 0:
        half = len(s) // 2
        left, right = int(s[:half]), int(s[half:])
        return evolve_stones(left, blinks - 1) + evolve_stones(right, blinks - 1)
    else:
        return evolve_stones(2024 * start, blinks - 1)

data = tuple(map(int, data.split()))

print(f"P1 {sum(evolve_stones(i, 25) for i in data)}")
print(f"P2 {sum(evolve_stones(i, 75) for i in data)}")

